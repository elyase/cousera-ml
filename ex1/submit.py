def submit(partId=None, webSubmit=False):
#SUBMIT Submit your code and output to the ml-class servers
#   SUBMIT() will connect to the ml-class server and submit your solution
    print '==\n== [ml-class] Submitting Solutions | Programming Exercise %s\n==\n' % homework_id()
    if not partId:
        partId = promptPart()

    # Check valid partId
    partNames = validParts()
    if not isValidPartId(partId):
        print '!! Invalid homework part selected.'
        print '!! Expected an integer from 1 to %d.' % len(partNames) + 1
        print '!! Submission Cancelled'
        return None

    login, password = loginPrompt()
    #TODO: add quick login functionality
    if not login:
        print '!! Submission Cancelled'
        return None

    print '\n== Connecting to ml-class ... '
    # Setup submit list
    submitParts = range(1, len(partNames)+1) if partId == len(partNames) + 1 else [partId]
    for thisPartId in submitParts:
        if not webSubmit:      # submit directly to server
            login, ch, signature, auxstring = getChallenge(login, thisPartId)
            if not login or not ch or not signature:
                # Some error occured, error string in first return element.
                print '\n!! Error: %s\n\n' % login
                return None
            # Attempt Submission with Challenge
            ch_resp = challengeResponse(login, password, ch)
            result, string = submitSolution(login, ch_resp, thisPartId,
                                            output(thisPartId, auxstring), source(thisPartId), signature)
            partName = partNames[thisPartId]
            print '\n== [ml-class] Submitted Assignment %s - Part %d - %s' % (homework_id(), thisPartId, partName)
            print '== %s' % string.strip()
        else:
            raise NotImplementedError('Web submission is not implemented')


# ================== CONFIGURABLES FOR EACH HOMEWORK ==================
def homework_id():
    return '4'


def validParts():
    return ['Feedforward and Cost Function',
            'Regularized Cost Function',
            'Sigmoid Gradient',
            'Neural Network Gradient (Backpropagation)',
            'Regularized Gradient']


def sources():
  # Returns the source files corresponding to each task
    return {'Feedforward and Cost Function': ['nnCostFunction.m'],
            'Regularized Cost Function': ['nnCostFunction.m'],
            'Sigmoid Gradient': ['sigmoidGradient.m'],
            'Neural Network Gradient (Backpropagation)': ['nnCostFunction.m'],
            'Regularized Gradient': ['nnCostFunction.m']}


def output(partId, auxstring):
    raise NotImplementedError


# ====================== SERVER CONFIGURATION ===========================

# ***************** REMOVE -staging WHEN YOU DEPLOY *********************
def site_url():
    return 'http://www.coursera.org/ml'


def challenge_url():
    return site_url() + '/assignment/challenge'


def submit_url():
    return site_url() + '/assignment/submit'

# ========================= CHALLENGE HELPERS =========================


def source(partId):
    # Concatenates source files for a given assignment
    src_files = sources()
    assert partId <= len(src_files)
    src = ''
    for f_name in src_files[partId]:
        try:
            with open(f_name) as f:
                src += f.read()
        except IOError:
            print 'Error opening %s (is it missing?)' % f_name
        src += '||||||||'
    return src


def isValidPartId(partId):
    return (partId >= 1) and (partId <= len(validParts()) + 1)


def promptPart():
    # Returns an integer representing the exercise to be submitted
    print '== Select which part(s) to submit:'
    partNames = validParts()
    srcFiles = sources()
    for i, part in enumerate(partNames):
        print '==   %s) %s [' % (i+1, part),
        print ' %s ', ' '.join(srcFiles[part]),
        print ']'
    print '==   %s) All of the above \n==\nEnter your choice [1-%s]: ' % (len(partNames) + 1, len(partNames) + 1)
    while True:
        try:
            partId = int(raw_input('Enter the number > ') or -1)
            break
        except ValueError:
            print 'Invalid number; please try again'
    if not isValidPartId(partId):
        partId = -1
    return partId


def getChallenge(email, part):
    raise NotImplementedError


def submitSolutionWeb(email, part, output, source):
    result = ''.join(['{"assignment_part_sid":"', base64encode(homework_id(), '-', str(part), ''), '",',
                      '"email_address":"', base64encode(email, ''), '",',
                      '"submission":"', base64encode(output, ''), '",',
                      '"submission_aux":"', base64encode(source, ''), '"', '}'])
    string = 'Web-submission'
    return result, string


def submitSolution(email, ch_resp, part, output, source, signature):
    raise NotImplementedError


# =========================== LOGIN HELPERS ===========================
def loginPrompt():
  # Prompt for password
  # @Yaser seems redundant
    login, password = basicPrompt()
    return login, password


def basicPrompt():
    login = raw_input('Login (Email address): ')
    password = raw_input('Password: ', 's')
    return login, password


def quickLogin(login, password):
    print 'You are currently logged in as %s.' % login
    answer = raw_input('Is this you? (y/n - type n to reenter password): ')
    if answer.uppercase().startwith('N'):
        return loginPrompt()


def challengeResponse(email, passwd, challenge):
    return sha1(challenge + passwd)


# =============================== SHA-1 ================================
def sha1(string):
    raise NotImplementedError


def bitadd(iA, iB):
    raise NotImplementedError


def bitrotate(iA, places):
    raise NotImplementedError


def base64encode(x, eol='\n'):
  #BASE64ENCODE Perform base64 encoding on a string.
    raise NotImplementedError


if __name__ == "__main__":
    submit()

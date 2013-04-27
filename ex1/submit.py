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
    return '1'


def validParts():
    return sources().keys()


def sources():
    from collections import OrderedDict
    # Returns the source files corresponding to each task
    return OrderedDict([('Warm up exercise ', ['warmUpExercise.py']),
                        ('Computing Cost (for one variable)', ['computeCost.m']),
                        ('Gradient Descent (for one variable)', ['gradientDescent.m']),
                        ('Feature Normalization', ['featureNormalize.m']),
                        ('Computing Cost (for multiple variables)', ['computeCostMulti.m']),
                        ('Gradient Descent (for multiple variables)', ['gradientDescentMulti.m']),
                        ('Normal Equations', ['normalEqn.m'])])


def output(partId, auxstring):
    raise NotImplementedError


# ====================== SERVER CONFIGURATION ===========================

# ***************** REMOVE -staging WHEN YOU DEPLOY *********************
def site_url():
    return 'https://class.coursera.org/ml-003'


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
    import urllib
    import urllib2
    params = {'assignment_part_sid': '-'.join([homework_id(), str(part)]),
              'email_address': email,
              'submission': base64encode(output, ''),
              'submission_aux': base64encode(source, ''),
              'challenge_response': ch_resp,
              'state': signature}
    encoded_params = urllib.urlencode(params)
    request = urllib2.Request(submit_url(), encoded_params)
    string = request.urlopen().read()
    # Parse str to read for success / failure
    result = 0
    return result, string


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
from struct import pack, unpack


def sha1(string):
    from numpy import uint32
    # Initialize variables:
    h0 = 1732584193
    h1 = 4023233417
    h2 = 2562383102
    h3 = 271733878
    h4 = 3285377520
    # Convert to word array
    strlen = len(string)
    numB = strlen * 8
    # Break string into chars and append the bit '1' to the message
    string += '\x80'
    string += '\x00' * ((56 - (strlen + 1) % 64) % 64)
    # append length of message
    string += pack('>Q', numB)
    # Process the message in successive 512-bit chunks:
    for i in xrange(0, len(string), 64):
        mW = [0] * 80
        for j in xrange(16):
            mW[j] = unpack('>I', string[i + j*4:i + j*4 + 4])[0]
        # Extend the sixteen 32-bit words into eighty 32-bit words:
        for j in xrange(16, 80):
            mW[j] = bitrotate(mW[j-3] ^ mW[j-8] ^ mW[j-14] ^ mW[j-16], 1)
        # Initialize hash value for this ch
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        # Main loop
        for i in xrange(80):
            if 0 <= i <= 19:
                f = d ^ (b & (c ^ d))
                k = uint32(1518500249)
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = uint32(1859775393)
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = uint32(2400959708)
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = uint32(3395469782)
            a, b, c, d, e = ((bitrotate(a, 5) + f + e + k + mW[i]) & 0xffffffff, a, bitrotate(b, 30), c, d)
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


def bitrotate(iA, places):
    return ((iA << places) | (iA >> (32 - places))) & 0xffffffff


def base64encode(x, eol='\n'):
    from base64 import b64encode
    return b64encode(x)


if __name__ == "__main__":
    submit()

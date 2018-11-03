def run(event, context):
    print('event', event)
    event['response']['autoConfirmUser'] = True
    event['response']['autoVerifyEmail'] = True
    return event

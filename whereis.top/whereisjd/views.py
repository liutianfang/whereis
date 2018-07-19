from django.http import HttpResponse
from django.http import JsonResponse
from whereisjd.models import *
import json
from django.views.decorators.csrf import csrf_exempt
import logging


START_MSG= "启动信息"

HELP_MSG= "帮助信息"
EXIT_MSG="好的，再见，我会一直等着你哦"


@csrf_exempt
def index(request):
    exmsg=""
    logger = logging.getLogger('django')
    response=JD_response()
    request_type=""
    requestVar={}
    log=JD_Whereis_Log()

    if request.method == 'POST':
        try:
            logger.info("POST process start ")

            requestVar = json.loads(request.body,encoding='utf-8')
            log.request=request.body
            log.ip=get_ip(request)
            log.header=meta(request)
            request_type = requestVar["request"]["type"]
        except  Exception:
            logger.info("POST  except= " +str(Exception ))
            response.shouldEndSession = True
            response.response["output"] = {"type": "PlainText", "text": EXIT_MSG}
            return JsonResponse(exit(), safe=False, )
    else: #GET

        return HttpResponse("service is working")

    # dispatch
    logger.info("request_type= "+request_type)
    response.contexts["last_request_type"] = request_type
    if(request_type=="LaunchRequest"):
        launchRequest(response,requestVar)
    elif(request_type=="IntentRequest"):
        intentRequest(response,logger,requestVar)
    elif(request_type=="SessionEndedRequest"):
        sessionEndedRequest(response )


    log.response=json.dumps(response.toJson(),ensure_ascii= False)
    log.exmsg= str(exmsg)
    log.save()
    return JsonResponse(response.toJson(), safe=False)

def launchRequest(response, requestVar={} ):
    response.response["output"] = {"type": "PlainText", "text": START_MSG}
    return

def intentRequest(response,logger,requestVar={}):
    logger.info("intentRequest process start ")
    intent = requestVar["request"]["intent"]["name"]
    response.contexts["intent"] = intent
    if intent == "Alpha.CancelIntent":
        response.shouldEndSession = True
        response.contexts["intentname"]="Alpha.CancelIntent"
        response.response["output"] = {"type": "PlainText", "text": EXIT_MSG}
        return
    elif intent == "Alpha.HelpIntent":
        response.response["output"] = {"type": "PlainText", "text": HELP_MSG}
        return

    elif intent == "remenber":
        remember(response,logger,requestVar)
        return

    return

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def meta(request):
    META = request.META
    info = ''
    for k, v in META.items():
	    info += '\r\n{} : {}\r\n'.format(k, v)
    return HttpResponse(info)

def sessionEndedRequest(response, request={}):
    response.shouldEndSession = True
    response.response["output"] = {"type": "PlainText", "text": EXIT_MSG}
    return ""

def help(requestVar={}):
    response=JD_response()
    response.response["output"]={"type":"PlainText","text":HELP_MSG}
    return response

def exit(request={}):
    response=JD_response()
    response.shouldEndSession=True
    response.response["output"]={"type":"PlainText","text":EXIT_MSG}
    return response.toJson()



def remember(response,logger,requestVar={}):

        msg = "您好，我已经记住"

        response.response["output"] = {"type": "PlainText", "text": msg}
        return


class JD_response:
    response={}
    session={}
    intent=""
    contexts = {}
    directives = []
    shouldEndSession=False


    # @classmethod
    def toJson(self):
        responseTemp={}
        responseTemp["version"] = "1.0"
        responseTemp["intent"] = self.intent
        responseTemp["contexts"] = self.contexts
        responseTemp["directives"] =self.directives
        responseTemp["shouldEndSession"] = self.shouldEndSession
        responseTemp["response"] = self.response

        return responseTemp

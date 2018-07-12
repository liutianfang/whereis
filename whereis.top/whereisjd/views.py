from django.http import HttpResponse
from django.http import JsonResponse
from whereisjd.models import *
import json
from django.views.decorators.csrf import csrf_exempt
import logging




WHEREIS_SKILL_ID="jd.alpha.skill.3ed0f131359e4b15970145d83c5a2e69"

HELP_MSG= "你好，我是小管家，你可以告诉我东西放在哪里。我会帮你记住的"
EXIT_MSG="好的，再见，我会一直等着你哦"

requestVar = {}

@csrf_exempt
def index(request):
    logger = logging.getLogger('django')
    response=JD_response()
    intent=""
    requestVar={}
    log=JD_Whereis_Log()

    if request.method == 'POST':
        try:
            logger.info("POST process start ")
            requestVar = json.loads(request.body)
            log.request=request.body
            log.ip=get_ip(request)
            log.header=meta(request)
            intent = requestVar["request"]["type"]
        except  Exception:
            logger.info("POST  except= " +str(Exception ))
            pass
    else:
        response.shouldEndSession = True
        response.intent = "exit"
        response.response["output"] = {"type": "PlainText", "text": EXIT_MSG}

        log.response = json.dumps(response.toJson(), ensure_ascii=False)
        log.save()
        return JsonResponse(exit(),safe=False,json_dumps_params={"ensure_ascii":False})
        # return HttpResponse(json.dumps(exit(),ensure_ascii=False),  content_type="application/json")

        # dispatch
    logger.info("intent= "+intent)
    if(intent=="LaunchRequest"):
        launchRequest(response,requestVar)
    elif(intent=="IntentRequest"):
        response.contexts["intent"]="IntentRequest"
        return_data=intentRequest(response,requestVar)
    elif(intent=="SessionEndedRequest"):
        return_data=sessionEndedRequest(response,requestVar )


    log.response=json.dumps(response.toJson(),ensure_ascii= False)
    log.save()
    return JsonResponse(response.toJson(), safe=False, json_dumps_params={"ensure_ascii": False})

def launchRequest(response, requestVar={} ):
    response.intent = "help"
    response.response["output"] = {"type": "PlainText", "text": HELP_MSG}

    return

def intentRequest(response,requestVar={}):

    if requestVar["request"]["intent"]["name"] == "Alpha.CancelIntent":
        response.shouldEndSession = True
        response.contexts["intentname"]="Alpha.CancelIntent"
        response.response["output"] = {"type": "PlainText", "text": EXIT_MSG}
        return
    elif requestVar["request"]["intent"]["name"] == "remember":
        pass

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

def sessionEndedRequest(request={}):
        return {}

def help(request={}):
    response=JD_response()
    response.intent="help"
    response.response["output"]={"type":"PlainText","text":HELP_MSG}
    return response

def exit(request={}):
    response=JD_response()
    response.shouldEndSession=True
    response.response["output"]={"type":"PlainText","text":EXIT_MSG}
    return response.toJson()


class JD_response:
    response={}
    session={}
    intent=""
    contexts = {}
    directives = {}
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


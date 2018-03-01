from django.shortcuts import render,HttpResponse

import json



def index(request):

    return render(request, 'index.html')
# Create your views here.
def yuanliti(request):

    dic = {
        #标题
        'dic1':{
            "id": 1,
            "text": "",
            "type": 1002,
            "userId": 0,
         },
        #正文
        'dic2':{
            "id": 2,
            "text": "",
            "type": 1001,
            "userId": 0,
        },
        #正文加粗
        'dic3':{
            "id": 3,
            "text": "",
            "type": 30011,
            "userId": 0,
        },
        #正文图片1
        'dic4':{
            "id": 4,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片2
        'dic5':{
            "id": 5,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片3
        'dic6':{
            "id": 6,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片4
        'dic7':{
            "id": 7,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正确答案
        'dic8':{
            "correctId": 13,
            "id": 8,
            "image": "",
            "text": "",
            "type": 30013,
            "userId": 0,
        },
        #错误答案
        'dic9':{
            "correctId": 0,
            "id": 9,
            "image": "",
            "text": "",
            "type": 30014,
            "userId": 0,
        },
        #过渡段/介绍段
        'dic10':{
            "id": 10,
            "text": "",
            "type": 6001,
            "userId": 0,
        },
        #解释／知识锦囊
        'dic11':{
            "id": 11,
            "text": "",
            "type": 6002,
            "userId": 0,
        },
        #解释加粗
        'dic12':{
            "id": 12,
            "text": "",
            "type": 30012,
            "userId": 0,
        },

        'dic13':{
            "id": 13,
            "type": 5001,
            "userId": 0,
        },
        #解释图片1
        'dic14':{
            "id": 14,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片2
        'dic15':{
            "id": 15,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片3
        'dic16':{
            "id": 16,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片4
        'dic17':{
            "id": 17,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
    }


    if request.method == "POST":

        action = request.POST.get('action', '')
        if action == 'tiankong':
            dic['dic1']['text'] = request.POST.get('title','')
            dic['dic2']['text'] = request.POST.get('content','')
            dic['dic3']['text'] = request.POST.get('bold1','')

            dic['dic4']['image'] = request.POST.get('image1','')
            dic['dic5']['image'] = request.POST.get('image2','')
            dic['dic6']['image'] = request.POST.get('image3','')
            dic['dic7']['image'] = request.POST.get('image4','')

            dic['dic8']['image'] = request.POST.get('rightimage','')
            dic['dic8']['text'] = request.POST.get('right','')

            dic['dic9']['image'] = request.POST.get('errorimage','')
            dic['dic9']['text'] = request.POST.get('error','')

            dic['dic10']['text'] = request.POST.get('intro','')
            dic['dic11']['text'] = request.POST.get('know','')
            dic['dic12']['text'] = request.POST.get('bold2','')

            dic['dic14']['image'] = request.POST.get('image5','')
            dic['dic15']['image'] = request.POST.get('image6','')
            dic['dic16']['image'] = request.POST.get('image7','')
            dic['dic17']['image'] = request.POST.get('image8','')
            return HttpResponse(json.dumps(dic,ensure_ascii=False))

    return render(request, 'yuanliti.html')


def anliti(request):
    dic = {
        #标题
        'dic1':{
            "id": 1,
            "text": "",
            "type": 1002,
            "userId": 0,
         },
         #正文
        'dic2':{
            "id": 2,
            "text": "",
            "type": 1001,
            "userId": 0,
        },
        #正文加粗
        'dic3':{
            "id": 3,
            "text": "",
            "type": 30011,
            "userId": 0,
        },
        #正文图片1
        'dic4':{
            "id": 4,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片2
        'dic5':{
            "id": 5,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片3
        'dic6':{
            "id": 6,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片4
        'dic7':{
            "id": 7,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正确答案
        'dic8':{
            "correctId": 2,
            "id": 8,
            "image": "",
            "text": "",
            "type": 30013,
            "userId": 0,
        },
        #错误答案
        'dic9':{
            "correctId": 0,
            "id": 9,
            "image": "",
            "text": "",
            "type": 30014,
            "userId": 0,
        },
        #错误答案
        'dic10':{
            "correctId": 0,
            "id": 10,
            "image": "",
            "text": "",
            "type": 30014,
            "userId": 0,
        },
        #错误答案
        'dic11':{
            "correctId": 0,
            "id": 11,
            "image": "",
            "text": "",
            "type": 30014,
            "userId": 0,
        },
        #过渡段/介绍段
        'dic12':{
            "id": 12,
            "text": "",
            "type": 6001,
            "userId": 0,
        },
        #解释／知识锦囊
        'dic13':{
            "id": 13,
            "text": "",
            "type": 6001,
            "userId": 0,
        },
        #解释加粗
        'dic14':{
            "id": 14,
            "text": "",
            "type": 30012,
            "userId": 0,
        },
        #解释图片1
        'dic15':{
            "id": 15,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片2
        'dic16':{
            "id": 16,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片3
        'dic17':{
            "id": 17,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片4
        'dic18':{
            "id": 18,
            "image": "",
            "type": 20012,
            "userId": 0,
        }

    }

    if request.method == "POST":

        action = request.POST.get('action', '')
        if action == 'anliti':

            dic['dic1']['text'] = request.POST.get('title','')
            dic['dic2']['text'] = request.POST.get('content','')
            dic['dic3']['text'] = request.POST.get('bold1','')

            dic['dic4']['image'] = request.POST.get('image1','')
            dic['dic5']['image'] = request.POST.get('image2','')
            dic['dic6']['image'] = request.POST.get('image3','')
            dic['dic7']['image'] = request.POST.get('image4','')

            dic['dic8']['image'] = request.POST.get('rightimage','')
            dic['dic8']['text'] = request.POST.get('right','')

            dic['dic9']['image'] = request.POST.get('error1image','')
            dic['dic9']['text'] = request.POST.get('error1','')

            dic['dic10']['image'] = request.POST.get('error2image','')
            dic['dic10']['text'] = request.POST.get('error2','')

            dic['dic11']['image'] = request.POST.get('error3image','')
            dic['dic11']['text'] = request.POST.get('error3','')

            dic['dic12']['text'] = request.POST.get('intro','')
            dic['dic13']['text'] = request.POST.get('know','')
            dic['dic14']['text'] = request.POST.get('bold2','')

            dic['dic18']['image'] = request.POST.get('image8','')
            dic['dic15']['image'] = request.POST.get('image5','')
            dic['dic16']['image'] = request.POST.get('image6','')
            dic['dic17']['image'] = request.POST.get('image7','')

            return HttpResponse(json.dumps(dic,ensure_ascii=False))

    return render(request, 'anliti.html')


def dapeiti(request):
    dic = {
        #标题
        'dic1':{
            "id": 1,
            "text": "",
            "type": 1002,
            "userId": 0,
         },
         #正文
        'dic2':{
            "id": 2,
            "text": "",
            "type": 1001,
            "userId": 0,
        },
        #正文加粗
        'dic3':{
            "id": 3,
            "text": "",
            "type": 30011,
            "userId": 0,
        },
        #正文图片1
        'dic4':{
            "id": 4,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片2
        'dic5':{
            "id": 5,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片3
        'dic6':{
            "id": 6,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #正文图片4
        'dic7':{
            "id": 7,
            "image": "",
            "type": 20011,
            "userId": 0,
        },
        #题目一
        'dic8':{
            "correctId": 14,
            "id": 8,
            "image": "",
            "text": "",
            "type": 3003,
            "userId": 0,
        },
        #题目二
        'dic9':{
            "correctId": 15,
            "id": 9,
            "image": "",
            "text": "",
            "type": 3003,
            "userId": 0,
        },
        #题目三
        'dic10':{
            "correctId": 16,
            "id": 10,
            "image": "",
            "text": "",
            "type": 3003,
            "userId": 0,
        },
        #题目四
        'dic11':{
            "correctId": 17,
            "id": 11,
            "image": "",
            "text": "",
            "type": 3003,
            "userId": 0,
        },
        #题目五
        'dic12':{
            "correctId": 18,
            "id": 12,
            "image": "",
            "text": "",
            "type": 3003,
            "userId": 0,
        },
        #题目六
        'dic13':{
            "correctId": 19,
            "id": 13,
            "image": "",
            "text": "",
            "type": 3003,
            "userId": 0,
        },
        #题目一答案
        'dic14':{
            "id": 14,
            "text": "",
            "type": 3001,
            "userId": 0,
        },
        #题目二答案
        'dic15':{
            "id": 15,
            "text": "",
            "type": 3001,
            "userId": 0,
        },
        #题目三答案
        'dic16':{
            "id": 16,
            "text": "",
            "type": 3001,
            "userId": 0,
        },
        #题目四答案
        'dic17':{
            "id": 17,
            "text": "",
            "type": 3001,
            "userId": 0,
        },
        #题目五答案
        'dic18':{
            "id": 18,
            "text": "",
            "type": 3001,
            "userId": 0,
        },
        #题目六答案
        'dic19':{
            "id": 19,
            "text": "",
            "type": 3001,
            "userId": 0,
        },
        #过渡段/介绍段
        'dic20':{
            "id": 20,
            "text": "",
            "type": 6001,
            "userId": 0,
        },
        #解释／知识锦囊
        'dic21':{
            "id": 21,
            "text": "",
            "type": 6001,
            "userId": 0,
        },
        #解释加粗
        'dic22':{
            "id": 22,
            "text": "",
            "type": 30012,
            "userId": 0,
        },
        #解释图片1
        'dic23':{
            "id": 23,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片2
        'dic24':{
            "id": 24,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片3
        'dic25':{
            "id": 25,
            "image": "",
            "type": 20012,
            "userId": 0,
        },
        #解释图片4
        'dic26':{
            "id": 26,
            "image": "",
            "type": 20012,
            "userId": 0,
        }

    }

    if request.method == "POST":

        action = request.POST.get('action', '')
        if action == 'dapeiti':

            dic['dic1']['text'] = request.POST.get('title','')
            dic['dic2']['text'] = request.POST.get('content','')
            dic['dic3']['text'] = request.POST.get('bold1','')

            dic['dic4']['image'] = request.POST.get('image1','')
            dic['dic5']['image'] = request.POST.get('image2','')
            dic['dic6']['image'] = request.POST.get('image3','')
            dic['dic7']['image'] = request.POST.get('image4','')

            dic['dic8']['image'] = request.POST.get('questionimage1','')
            dic['dic8']['text'] = request.POST.get('question1','')
            dic['dic9']['image'] = request.POST.get('questionimage2','')
            dic['dic9']['text'] = request.POST.get('question2','')
            dic['dic10']['image'] = request.POST.get('questionimage3','')
            dic['dic10']['text'] = request.POST.get('question3','')
            dic['dic11']['image'] = request.POST.get('questionimage4','')
            dic['dic11']['text'] = request.POST.get('question4','')
            dic['dic12']['image'] = request.POST.get('questionimage5','')
            dic['dic12']['text'] = request.POST.get('question5','')
            dic['dic13']['image'] = request.POST.get('questionimage6','')
            dic['dic13']['text'] = request.POST.get('question6','')

            dic['dic14']['text'] = request.POST.get('answer1','')
            dic['dic15']['text'] = request.POST.get('answer2','')
            dic['dic16']['text'] = request.POST.get('answer3','')
            dic['dic17']['text'] = request.POST.get('answer4','')
            dic['dic18']['text'] = request.POST.get('answer5','')
            dic['dic19']['text'] = request.POST.get('answer6','')

            dic['dic20']['text'] = request.POST.get('intro','')
            dic['dic21']['text'] = request.POST.get('know','')
            dic['dic22']['text'] = request.POST.get('bold2','')

            dic['dic23']['image'] = request.POST.get('image5','')
            dic['dic24']['image'] = request.POST.get('image6','')
            dic['dic25']['image'] = request.POST.get('image7','')
            dic['dic26']['image'] = request.POST.get('image8','')

            return HttpResponse(json.dumps(dic,ensure_ascii=False))

    return render(request, 'dapeiti.html')

def shuomingti(request):
    dic = {
        #标题
        'dic1':{
            "id": 1,
            "text": "",
            "type": 1002,
            "userId": 0,
         },
         #对话1
        'dic2':{
            "id": 2,
            "text": "",
            "type": 4001,
            "userId": 0,
        },
        #问题一
        'dic3':{
            "id": 3,
            "text": "",
            "type": 4001,
            "userId": 0,
        },
        #问题一正确回答
        'dic4':{
            "id": 4,
            "type": 3004,
            "text": "",
            "userId": 0,
            "parentId":3,
            "correctId":3
        },
        #问题一回答二
        'dic5':{
            "id": 5,
            "type": 3004,
            "text": "",
            "userId": 0,
            "parentId":3,
            "correctId":0
        },
        #问题一回答一的下一步说明
        'dic6':{
            "id": 6,
            "type": 4001,
            "text": "",
            "userId": 0,
            "parentId":4
        },
        #问题一回答二的下一步说明
        'dic7':{
            "id": 7,
            "type": 4001,
            "text": "",
            "userId": 0,
            "parentId":5
        },
        #第二个对话
        'dic8':{
            "id": 8,
            "text": "",
            "type": 4001,
            "userId": 0,
        },
        #问题二
        'dic9':{
            "id": 9,
            "text": "",
            "type": 4001,
            "userId": 0,
        },
        #问题二正确回答
        'dic10':{
            "id": 10,
            "text": "",
            "type": 3004,
            "userId": 0,
            "parentId":9,
            "correctId":9
        },
        #问题二错误回答
        'dic11':{
            "id": 11,
            "text": "",
            "type": 3004,
            "userId": 0,
            "parentId":9，
            "correctId":0
        },
        #问题二回答一的下一步说明
        'dic12':{
            "id": 12,
            "text": "",
            "type": 4001,
            "userId": 0,
            "parentId":10
        },
        #问题二回答二的下一步说明
        'dic13':{
            "id": 13,
            "text": "",
            "type": 4001,
            "userId": 0,
            "parentId":11
        },
        #第三个对话
        'dic14':{
            "id": 14,
            "text": "",
            "type": 4001,
            "userId": 0,
        },
        #第一个图片
        'dic15':{
            "id": 15,
            "image":"",
            "type": 2001,
            "userId": 0,
        },
        #第二个图片
        'dic16':{
            "id": 16,
            "image":"",
            "type": 2001,
            "userId": 0,
        },
        #第三个图片
        'dic17':{
            "id": 17,
            "image":"",
            "type": 2001,
            "userId": 0,
        },
        #第四个图片
        'dic18':{
            "id": 18,
            "image":"",
            "type": 2001,
            "userId": 0,
        },

    }

    if request.method == "POST":

        action = request.POST.get('action', '')
        if action == 'shuomingti':

            dic['dic1']['text'] = request.POST.get('title','')


            texta1 = request.POST.get('duihua1','')
            texta1.replace('。','。\\r\\n')

            dic['dic2']['text'] = texta1
            dic['dic3']['text'] = request.POST.get('question1','')

            dic['dic4']['text'] = request.POST.get('right1','')
            dic['dic5']['text'] = request.POST.get('error1','')
            dic['dic6']['text'] = request.POST.get('rightshuoming1','')
            dic['dic7']['text'] = request.POST.get('errorshuoming1','')


            texta2 = request.POST.get('duihua2','')
            texta2.replace('。','。\\r\\n')

            dic['dic8']['text'] = texta2
            dic['dic9']['text'] = request.POST.get('question2','')

            dic['dic10']['text'] = request.POST.get('right2','')
            dic['dic11']['text'] = request.POST.get('error2','')

            dic['dic12']['text'] = request.POST.get('rightshuoming2','')
            dic['dic13']['text'] = request.POST.get('errorshuoming2','')


            texta3 = request.POST.get('duihua3','')
            texta3.replace('。','。\\r\\n')
            dic['dic14']['text'] = texta3


            dic['dic15']['image'] = request.POST.get('image1','')
            dic['dic16']['image'] = request.POST.get('image2','')
            dic['dic17']['image'] = request.POST.get('image2','')
            dic['dic18']['image'] = request.POST.get('image3','')

            return HttpResponse(json.dumps(dic,ensure_ascii=False))

    return render(request, 'shuomingti.html')
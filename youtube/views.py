from django.shortcuts import render, redirect
from django.http import HttpResponse
import joblib
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    html = '''
<style>
table, th, td {
  border: 1px solid black;
  padding: 10px;
  font-size: 16px;
  color: black;
}
</style>

<h1><center>예측하기</center></h1>
<form action="/youtube/predict">
<center>
<table style="width:100%" >
	<tr style="background-color:'#f2f2f2">
    <th style="width:40%"></th>
    <th style="width:60%">선호 채널의 콘텐츠 예측하기</th>
  </tr>
  <tr>
    <td><center>채널의 구독자수</center></td>
    <td><input type="text" name="view_sub"></td>
  </tr>
  <tr>
    <td><center>한 영상 당 본인의 조회수</center></td>
    <td><input type="text" name="video_nums"></td>
  </tr>
  <tr>
    <td><center>유튜버 성별</center></td>
    <td>
    <input type="radio" id="male" name="male" value="1">
    <label for="male">Male</label><br>
    <input type="radio" id="female" name="male" value="0">
    <label for="female">Female</label><br>
    </td>
  </tr>
  <tr>
    <td><center>여러명/동물 유튜버</center></td>
    <td>
    <input type="radio" id="multisex1" name="multisex" value="1">
    <label for="multisex1">O</label><br>
    <input type="radio" id="multisex2" name="multisex" value="0">
    <label for="multisex2">X</label><br>
    </td>
  </tr>
</table>
</center>
<div style="float:right; margin:10px;"><input type="submit" value="확인"></div>

'''
    return HttpResponse(html)
    '''
    return render(request, 'index.html', {})
    '''

@csrf_exempt
def predict(request):
    try:
        view_sub = request.GET['view_sub']
    except:
        view_sub = '0'
    view_sub = int(view_sub)
    try:
        video_nums = request.GET['video_nums']
    except:
        video_nums = '0'
    video_nums = int(video_nums)
    try:
        male = request.GET['male']
    except:
        male = '1'
    male = int(male)
    try:
        multisex = request.GET['multisex']
    except:
        multisex = '0'
    multisex = int(multisex)
    Person = [[view_sub, video_nums, male, multisex]]

    # 모델 사용하기
    RF_model = joblib.load('c:/Users/python/myproject/youtube/RF_model.model')
    pred = RF_model.predict(Person)
    df_name = ['animal', 'beauty', 'education', 'food', 'game', 'kids', 'music', 'people', 'sports']
    contents = df_name[pred[0]]
    return render(request, 'youtube/predict.html',{'contents':contents})

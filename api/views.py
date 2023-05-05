from pathlib import Path
import pandas as pd
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
BASE_DIR = Path(__file__).resolve().parent.parent
def pred(request, id = None):
    ans = id
    path1 = os.path.join(BASE_DIR, 'api/output/output.csv')
    df = pd.read_csv(path1)
    dic = df.set_index('IDLink').T.to_dict('list')
    buff = dic[ans]
    return JsonResponse({"SentimentTitle": buff[0], "SentimentHeadline": buff[1],})
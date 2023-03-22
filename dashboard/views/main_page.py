from django.shortcuts import render
from django.views import View


class MainPage(View):


    def get(self,request):


        subes = [
            {
                "name": "TEST SUBE ADI",
                "results": [
                    {"name": "sincere", "result": 20},  # içten
                    {"name": "reputable", "result": 20},  # saygınlık
                    {"name": "powerful", "result": 20},  # güç
                    {"name": "competence", "result": 20},  # yetkinlik
                    {"name": "excitement", "result": 20},  # heyecan
                ]
            },
            {
                "name": "TEST SUBE ADI",
                "results": [
                    {"name": "sincere", "result": 20},  # içten
                    {"name": "reputable", "result": 20},  # saygınlık
                    {"name": "powerful", "result": 20},  # güç
                    {"name": "competence", "result": 20},  # yetkinlik
                    {"name": "excitement", "result": 20},  # heyecan
                ]
            },
            {
                "name": "TEST SUBE ADI",
                "results": [
                    {"name": "sincere", "result": 20},  # içten
                    {"name": "reputable", "result": 20},  # saygınlık
                    {"name": "powerful", "result": 20},  # güç
                    {"name": "competence", "result": 20},  # yetkinlik
                    {"name": "excitement", "result": 20},  # heyecan
                ]
            },
            {
                "name": "TEST SUBE ADI",
                "results": [
                    {"name": "sincere", "result": 20},  # içten
                    {"name": "reputable", "result": 20},  # saygınlık
                    {"name": "powerful", "result": 20},  # güç
                    {"name": "competence", "result": 20},  # yetkinlik
                    {"name": "excitement", "result": 20},  # heyecan
                ]
            }
        ]
        return render(request,"dashboard.html",context={
            "subes":subes
        })


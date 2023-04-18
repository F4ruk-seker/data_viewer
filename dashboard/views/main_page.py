from django.shortcuts import render
from django.views import View
from product_operation.models import Office
import folium


class MainPage(View):

    def get(self,request):
        __map = folium.Map(location=[39.92077, 32.85411],height=250)


        office_data = []

        for office in Office.objects.all():
            office_data.append({
                "name":office.name,
                "id":office.id,
                "data":office.performance.get_metric_as_percentile_ord_isgyh()
            })

        return render(request,"dashboard_second.html",context={
            "office_data":office_data,
            "map":__map._repr_html_()
        })


from django.db import models


class PerformanceMetric(models.Model):
    sincere_count = models.IntegerField(default=0)
    reputable_count = models.IntegerField(default=0)
    powerful_count = models.IntegerField(default=0)
    competence_count = models.IntegerField(default=0)
    excitement_count = models.IntegerField(default=0)

    def get_total_metric(self):
        return self.excitement_count+self.competence_count+self.powerful_count+self.sincere_count+self.reputable_count

    def get_metric_as_percentile_ord_isgyh(self):
        total = self.get_total_metric()
        return [
             int(round((self.sincere_count / total) * 100, 2)),  # içten
             int(round((self.reputable_count / total) * 100, 2)),  # saygınlık
             int(round((self.powerful_count / total) * 100, 2)),  # güç
             int(round((self.competence_count / total) * 100, 2)),  # yetkinlik
             int(round((self.excitement_count / total) * 100, 2)),  # heyecan
        ]
    def get_metric(self):
        total = self.get_total_metric()
        return [
            {"name": "sincere", "result": round((self.sincere_count / total) * 100, 2)},  # içten
            {"name": "reputable", "result": round((self.reputable_count / total) * 100, 2)},  # saygınlık
            {"name": "powerful", "result": round((self.powerful_count / total) * 100, 2)},  # güç
            {"name": "competence", "result": round((self.competence_count / total) * 100, 2)},  # yetkinlik
            {"name": "excitement", "result": round((self.excitement_count / total) * 100, 2)},  # heyecan
        ]


class SubMetric(models.Model):
    pass

"""
{"name": "sincere", "result": 20},  # içten
{"name": "reputable", "result": 20},  # saygınlık
{"name": "powerful", "result": 20},  # güç
{"name": "competence", "result": 20},  # yetkinlik
{"name": "excitement", "result": 20},  # heyecan
"""
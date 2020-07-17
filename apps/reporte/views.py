from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.db.models import Q

from apps.proceso.models import Proceso
from apps.acta.models import Acta
from django.contrib.auth.mixins import LoginRequiredMixin


class ReporteView(LoginRequiredMixin, ListView):
    model = Proceso
    template_name = 'reporte/reportes.html'

    def post(self, request):
        try:
            fecha = request.POST['fecha']
            # canon = request.POST['canon']
            mycontent = {}
            date = []
            if fecha != '':
                ordinario = Proceso.objects.filter(
                    Q(tipo__nombre='Ordinario') & Q(fecha__year=fecha)).count()
                documental = Proceso.objects.filter(
                    Q(tipo__nombre='Documental') & Q(fecha__year=fecha)).count()
                rato = Proceso.objects.filter(
                    Q(tipo__nombre='Rato y no Consumado') & Q(fecha__year=fecha)).count()
                breve = Proceso.objects.filter(
                    Q(tipo__nombre='Breve') & Q(fecha__year=fecha)).count()
                canon1 = Acta.objects.filter(
                    Q(canon__idcanon='1083') & Q(fecha__year=fecha)).count()
                canon2 = Acta.objects.filter(
                    Q(canon__idcanon='1084') & Q(fecha__year=fecha)).count()
                canon3 = Acta.objects.filter(
                    Q(canon__idcanon='1085') & Q(fecha__year=fecha)).count()
                canon4 = Acta.objects.filter(
                    Q(canon__idcanon='1086') & Q(fecha__year=fecha)).count()
                canon5 = Acta.objects.filter(
                    Q(canon__idcanon='1087') & Q(fecha__year=fecha)).count()
                canon6 = Acta.objects.filter(
                    Q(canon__idcanon='1088') & Q(fecha__year=fecha)).count()
                canon7 = Acta.objects.filter(
                    Q(canon__idcanon='1089') & Q(fecha__year=fecha)).count()
                canon8 = Acta.objects.filter(
                    Q(canon__idcanon='1090') & Q(fecha__year=fecha)).count()
                canon9 = Acta.objects.filter(
                    Q(canon__idcanon='1091') & Q(fecha__year=fecha)).count()
                canon10 = Acta.objects.filter(
                    Q(canon__idcanon='1092') & Q(fecha__year=fecha)).count()
                canon11 = Acta.objects.filter(
                    Q(canon__idcanon='1093') & Q(fecha__year=fecha)).count()
                canon12 = Acta.objects.filter(
                    Q(canon__idcanon='1094') & Q(fecha__year=fecha)).count()
                canon13 = Acta.objects.filter(
                    Q(canon__idcanon='1095.1') & Q(fecha__year=fecha)).count()
                canon14 = Acta.objects.filter(
                    Q(canon__idcanon='1095.2') & Q(fecha__year=fecha)).count()
                canon15 = Acta.objects.filter(
                    Q(canon__idcanon='1095.3') & Q(fecha__year=fecha)).count()
                canon16 = Acta.objects.filter(
                    Q(canon__idcanon='1096') & Q(fecha__year=fecha)).count()
                canon17 = Acta.objects.filter(
                    Q(canon__idcanon='1097 § 1') & Q(fecha__year=fecha)).count()
                canon18 = Acta.objects.filter(
                    Q(canon__idcanon='1097 § 2') & Q(fecha__year=fecha)).count()
                canon19 = Acta.objects.filter(
                    Q(canon__idcanon='1098') & Q(fecha__year=fecha)).count()
                canon20 = Acta.objects.filter(
                    Q(canon__idcanon='1099') & Q(fecha__year=fecha)).count()
                canon21 = Acta.objects.filter(
                    Q(canon__idcanon='1100') & Q(fecha__year=fecha)).count()
                canon22 = Acta.objects.filter(
                    Q(canon__idcanon='1101 § 1') & Q(fecha__year=fecha)).count()
                canon23 = Acta.objects.filter(
                    Q(canon__idcanon='1101 § 2') & Q(fecha__year=fecha)).count()
                canon24 = Acta.objects.filter(
                    Q(canon__idcanon='1102 § 1') & Q(fecha__year=fecha)).count()
                canon25 = Acta.objects.filter(
                    Q(canon__idcanon='1102 § 2') & Q(fecha__year=fecha)).count()
                canon26 = Acta.objects.filter(
                    Q(canon__idcanon='1102 § 3') & Q(fecha__year=fecha)).count()
                canon27 = Acta.objects.filter(
                    Q(canon__idcanon='1103') & Q(fecha__year=fecha)).count()
                canon28 = Acta.objects.filter(
                    Q(canon__idcanon='1104') & Q(fecha__year=fecha)).count()
                canon29 = Acta.objects.filter(
                    Q(canon__idcanon='1105') & Q(fecha__year=fecha)).count()
                canon30 = Acta.objects.filter(
                    Q(canon__idcanon='1106') & Q(fecha__year=fecha)).count()
                canon31 = Acta.objects.filter(
                    Q(canon__idcanon='1107') & Q(fecha__year=fecha)).count()
                canon32 = Acta.objects.filter(
                    Q(canon__idcanon='1108') & Q(fecha__year=fecha)).count()

                mycontent = {'Tipo Ordinario': ordinario, 'Tipo Documental': documental,
                             'Tipo Rato': rato, 'Tipo Breve': breve, 'Canon 1083': canon1,
                             'Canon 1084': canon2, 'Canon 1085': canon3, 'Canon 1086': canon4,
                             'Canon 1087': canon5, 'Canon 1088': canon6, 'Canon 1089': canon7,
                             'Canon 1090': canon8, 'Canon 1091': canon9, 'Canon 1092': canon10,
                             'Canon 1093': canon11, 'Canon 1094': canon12, 'Canon 1095.1': canon13,
                             'Canon 1095.2': canon14, 'Canon 1095.3': canon15, 'Canon 1096': canon16,
                             'Canon 1097 § 1': canon17, 'Canon 1097 § 2': canon18, 'Canon 1098': canon19,
                             'Canon 1099': canon20, 'Canon 1100': canon21, 'Canon 1101 § 1': canon22,
                             'Canon 1101 § 2': canon23, 'Canon 1102 § 1': canon24, 'Canon 1102 § 2': canon25,
                             'Canon 1102 § 3': canon26, 'Canon 1103': canon27, 'Canon 1104': canon28,
                             'Canon 1105': canon29, 'Canon 1106': canon30, 'Canon 1107': canon31, 
                             'Canon 1108': canon32
                             }

                date.append({'fecha': fecha})
            return render(request, "reporte/reportes.html", {'date': date, 'mycontent': mycontent})
        except ValueError:
            return render(request, "reporte/reportes.html")

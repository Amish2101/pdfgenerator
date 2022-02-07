from curses import erasechar
import re
from io import StringIO, BytesIO
from django.forms import model_to_dict

from rest_framework import status
from rest_framework.views import APIView

from django.http import Http404

from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse
from user.models import reports, user, pathology, cbcreport

from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle

from textwrap import wrap


class SimpleExample(APIView):

    renderer_classes = (PDFRenderer, )  

    def get_object(self, pk):
        try:
            return reports.objects.get(pk=pk)
        except reports.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, *args, **kwargs):
        report_name = self.get_object(pk)
        patholog = pathology.objects.filter(
            report_name = self.get_object(pk)
        )
        cbc = cbcreport.objects.get(pk = pk)
        pdf = BytesIO()

        dec = 30
        pos = 820
        gen_pdf = canvas.Canvas(pdf)
        gen_pdf.setTitle('Mohit Wellness Pvt Ltd')

        

        gen_pdf.drawString(250, pos, 'Mohit Wellness Pvt Ltd')
        gen_pdf.drawString(0,pos - 10, '-'*150)
        pos -= dec
        gen_pdf.drawString(250, pos + 5, f'pasentname :- {request.user}')
        gen_pdf.drawString(0,pos - 10, '-'*150)
        pos -= dec
        gen_pdf.drawString(250, pos + 5, f'report name :- {report_name}')
        gen_pdf.drawString(0,pos - 10, '-'*150)
        pos -= dec

        gen_pdf.drawString(50, pos, f'Parameter')
        gen_pdf.drawString(220, pos, f'Result')
        gen_pdf.drawString(300, pos, f'Unit')
        gen_pdf.drawString(400, pos, f'Biological Reference Interval')
        pos -= dec
        gen_pdf.drawString(50, pos, f'Hemoglobin')
        gen_pdf.drawString(220, pos, f'{cbc.hb}')
        gen_pdf.drawString(280, pos, f'L')
        gen_pdf.drawString(300, pos, f'gm%')
        gen_pdf.drawString(400, pos, f'11.0 - 14.0')
        pos -= dec
        gen_pdf.drawString(50, pos, f'total RBC count')
        gen_pdf.drawString(220, pos, f'{cbc.rbc}')
        gen_pdf.drawString(280, pos, f'H')
        gen_pdf.drawString(300, pos, f'million/cmm')
        gen_pdf.drawString(400, pos, f'4 - 5.2')
        pos -= dec
        gen_pdf.drawString(50, pos, f'total wbc count')
        gen_pdf.drawString(220, pos, f'{cbc.wbc}')
        gen_pdf.drawString(300, pos, f'/cmm')
        gen_pdf.drawString(400, pos, f'5000 - 15000')
        pos -= dec
        gen_pdf.drawString(50, pos, f'platelet count')
        gen_pdf.drawString(220, pos, f'{cbc.platelet}')
        gen_pdf.drawString(280, pos, f'H')
        gen_pdf.drawString(300, pos, f'/cmm')
        gen_pdf.drawString(400, pos, f'150000 - 450000')
        pos -= dec
        gen_pdf.drawString(50, pos, f'hematocrit')
        gen_pdf.drawString(220, pos, f'{cbc.hematocrit}')
        gen_pdf.drawString(280, pos, f'L')
        gen_pdf.drawString(300, pos, f'%')
        gen_pdf.drawString(400, pos, f'34 - 40')
        pos -= dec
        gen_pdf.drawString(50, pos, f'MCV')
        gen_pdf.drawString(220, pos, f'{cbc.mcv}')
        gen_pdf.drawString(280, pos, f'L')
        gen_pdf.drawString(300, pos, f'fl')
        gen_pdf.drawString(400, pos, f'75 - 87')
        pos -= dec
        gen_pdf.drawString(50, pos, f'MCH')
        gen_pdf.drawString(220, pos, f'{cbc.mch}')
        gen_pdf.drawString(280, pos, f'L')
        gen_pdf.drawString(300, pos, f'pg')
        gen_pdf.drawString(400, pos, f'25 - 30')
        pos -= dec
        gen_pdf.drawString(50, pos, f'MCHC')
        gen_pdf.drawString(220, pos, f'{cbc.mchc}')
        gen_pdf.drawString(280, pos, f'L')
        gen_pdf.drawString(300, pos, f'%')
        gen_pdf.drawString(400, pos, f'32 - 36')
        pos -= dec    
        gen_pdf.drawString(50, pos, f'DIFFERNTIAL WBC COUNT (Manual By Microscopy)')  
        pos -= dec   
        gen_pdf.drawString(50, pos, f'Neutrophils')         
        gen_pdf.drawString(220, pos, f'{cbc.neutrophils}')
        gen_pdf.drawString(300, pos, f'%')
        gen_pdf.drawString(400, pos, f'25 - 70')    
        pos -= dec        
        gen_pdf.drawString(50, pos, f'Lymphocytes')
        gen_pdf.drawString(220, pos, f'{cbc.lymphocytes}')
        gen_pdf.drawString(300, pos, f'%')
        gen_pdf.drawString(400, pos, f'30 - 70')   
        pos -= dec         
        gen_pdf.drawString(50, pos, f'Eosinophils')
        gen_pdf.drawString(220, pos, f'{cbc.eosinophils}')
        gen_pdf.drawString(300, pos, f'%')
        gen_pdf.drawString(400, pos, f'0 - 4') 
        pos -= dec           
        gen_pdf.drawString(50, pos, f'Monocytes')
        gen_pdf.drawString(220, pos, f'{cbc.monocytes}')
        gen_pdf.drawString(300, pos, f'%')
        gen_pdf.drawString(400, pos, f'0 - 10') 
        pos -= dec           
        gen_pdf.drawString(50, pos, f'Basophils')
        gen_pdf.drawString(220, pos, f'{cbc.basophils}')
        gen_pdf.drawString(300, pos, f'%')
        gen_pdf.drawString(400, pos, f'0 - 1') 
        pos -= dec           
        gen_pdf.drawString(50, pos, f'Platelets appear on the smear')
        gen_pdf.drawString(220, pos, f'{cbc.paots}')
        pos -= dec
        gen_pdf.drawString(50, pos, f'PS FOR MP')
        gen_pdf.drawString(220, pos, f'{cbc.pfm}')
        pos -= dec
        gen_pdf.drawString(50, pos, f'Microcytosis')
        gen_pdf.drawString(220, pos, f'{cbc.microcytosis}')
        pos -= dec
        gen_pdf.drawString(50, pos, f'Hyphochromia')
        gen_pdf.drawString(220, pos, f'{cbc.hyphochromia}')
        pos -= dec
        gen_pdf.drawString(50, pos, f'Anisocytosis')
        gen_pdf.drawString(220, pos, f'{cbc.anisocytosis}')
        pos -= dec
        gen_pdf.drawString(50, pos, f'few target cells seen')
        gen_pdf.drawString(220, pos, f'microcytic hypochromic anaemia')

        pos -= dec
        gen_pdf.showPage()



        dec = 30
        pos = 800

        gen_pdf.drawString(50, pos, 'pothology :-')
        pos -= dec

        for i in range(0, len(patholog)):
            t = gen_pdf.beginText()
            dec = 50
            t.setTextOrigin(50, pos)
            pos -= dec
            text1 = patholog[i]
            print(text1)
            wraped_text = "\n".join(wrap(str(text1), 90))
            t.textLines(wraped_text)
            gen_pdf.drawText(t)

        
        print(pos)



        gen_pdf.showPage()
        gen_pdf.save()

        return PDFResponse(pdf.getvalue(),file_name=f'{request.user}_report',status=status.HTTP_200_OK)
    

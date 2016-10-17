# -*- coding: utf-8 -*-
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import csv
from db import UserProfile
import time

with open('1point3acres.csv',"wb") as f:
    start_time=time.time()
    csv_writer=csv.writer(f)
    csv_writer.writerow([
                '申请学校',
                '学位',
                '专业',
                '申请结果',
                '入学时间',
                '通知时间',
                '本科专业',
                '本科大学',
                '本科GPA',
                'master专业',
                'master大学',
                'masterGPA',
                'TOEFL',
                'GRE',
                '其他',
                '来源',
                ])
    for status in UserProfile.objects:
        csv_writer.writerow([
            status.wanna_university,
            status.wanna_diploma,
            status.wanna_subject,
            status.result,
            status.leave_time,
            status.undergraduate_subject,
            status.undergraduate_university,
            status.undergraduate_GPA,
            status.ms_subject,
            status.ms_university,
            status.ms_GPA,
            status.toefl,
            status.GRE,
            status.something,
            status.Source
        ])
    print "to csv,it cost:",time.time()-start_time

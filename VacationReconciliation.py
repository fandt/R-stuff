def read_vacation():
  from datetime import datetime
  import csv
  import fileinput
  import os
  import Tkinter, tkFileDialog
  root = Tkinter.Tk()
  currentfile = tkFileDialog.askopenfilename(parent=root,initialdir="C:path",title='Choose the CURRENT Vacation Accrual Report')
  previousfile = tkFileDialog.askopenfilename(parent=root,initialdir="C:path",title='Choose the PREVIOUS Vacation Accrual Report')


  current=csv.reader(open(currentfile))
  previous=csv.reader(open(previousfile))
  marker=0
  for row in current:
    marker = marker +1
    if marker > 1:
      
      #inputdate = raw_input('paydate? yyyy,mm,dd\n')
      cdate = datetime.today()
      sdateexcel = row[6]
      if sdateexcel == "" and row[0]!="Grand Totals" and row[0]!="Total":
           print row[0] +" Seniority is blank  "+str(row[3])+" and "+ str(row[7]) + " taken"
           continue
      try:
        smonth, sday, syear = sdateexcel.split("/")
        sdate = datetime(int(syear),int(smonth),int(sday))
        seniority = cdate.toordinal() - sdate.toordinal()
      except:
        continue
      try:
        #test for neg balance
        bal = float(row[3])
        if row[3] != "" and float(row[3])==0.00:
            if seniority >= 180:
                print row[0] + " Bal= 0 @ " + str(sdateexcel)
                continue
      except:
        print row[0] + " Bal = negative"
        continue
      
      try:
        #test for neg float balance
        bal = float(row[4])
      except:
        print row[0] + " Float = negative"
        continue
      
      if seniority >= 180:
          for prow in previous:

            #test for leaves

            if prow[0] <= row[0] or prow[0]=='Name':
              if prow[0] == row[0]:
                  accum = round(float(row[3]) - float(prow[3]),2)
                  faccum = round(float(row[4])-float(prow[4]),2)
                  vtaken = float(row[7])
                  ftaken = float(row[8])
                  accum = round(accum+vtaken,2)
                  faccum = round(faccum+ftaken,2)

                  if row[2] == "FT" or row[2] == "FTU":
                      if seniority >= 3650:
                          if accum != 6.67:
                            print row[0] + "     Accumulated " + str(faccum) + " @ seniority >10 yrs, bal = " + str(row[3])
                          break
                      elif seniority >= 1825:
                          if accum != 5:
                            print row[0] + "     Accumulated " + str(faccum) + " @ seniority >5 yrs "
                          break
                      elif accum != 3.33:
                          print row[0] + "     Accumulated " + str(faccum) + " @ seniority " + str(sdateexcel)
                      break
                  if row[2] == "FT75" or row[2] == "PT75":
                      if seniority >= 3650:
                          if accum != 5:
                            print row[0] + "      Accumulated " + str(faccum) + " @ >10 yrs, 75%  "
                          break
                      elif seniority >= 1825:
                          if accum != 3.75:
                            print row[0] + "      Accumulated " + str(faccum) + " @ >5 yrs, 75% "
                          break
                      elif accum != 2.5:
                          print row[0] + "     Accumulated " + str(faccum) + " @ <5 yrs, 75% "
                      break
                  if row[2] == "PT50":
                       if seniority >= 3650:
                          if accum != 3.33:
                            print row[0] + "     Accumulated " + str(faccum) + " @ >10 yrs, 50% "
                          break
                       elif seniority >= 1825:
                          if accum != 2.5:
                            print row[0] + "     Accumulated " + str(faccum) + " @ >5 yrs, 50% "
                          break
                       elif accum != 1.66:
                          print row[0] + "     Accumulated " + str(faccum) + " @ <5 yrs, 50%  " 
                       break
                  if row[2] == "TEMP":
                       print row[0] + "     Accumulated " + str(faccum)
                  elif accum == 0:
                    print row[0] + "     Accumulated 0 and " + row[2]
                  break

  current=csv.reader(open(currentfile))
  previous=csv.reader(open(previousfile))
  
  for row in current:
      leavemarker = 0
      for prow in previous:
          if prow[0] == row[0]:
            leavemarker = 1
            previous=csv.reader(open(previousfile))
            break

      if leavemarker == 0 and prow[0]== "Total":
          print str(row[0]) + " was on leave " 
          previous=csv.reader(open(previousfile))
          
  raw_input("press enter to exit")


read_vacation()

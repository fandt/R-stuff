def test_sums():
  import csv
  import Tkinter, tkFileDialog
  import os
  file = "C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon"
  krecon = open(file,"w+")
  root = Tkinter.Tk()
  marker = 0
  deductotal = 0
  invoicetotal = 0
  InvoiceType = "Kaiser"
  deductSS = 0
  name = "blank"
  global found
  oddeven = 0
  missing = "blank"
  currentfile = tkFileDialog.askopenfilename(parent=root,initialdir="C:/Users/rmorganstern/Documents/Medent Reconcile/",title='Choose the current deduction report')
  deductionfile = csv.reader(open(currentfile))
  for drow in deductionfile:
    if marker > 0:
        
        try:
          deductEE = float(drow[3])
          deductER = float(drow[4])
          name = drow[2]
          deductotal = round((deductotal + deductEE + deductER),2)
          deductSS = drow[6]
        except:
          pass
        if marker%2 == 0 :
          with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write(str(invoicetotal)+"\t"+InvoiceType+"\n")
          #print
          out = str(deductSS)+"\t"+str(name)+"\t"+str(deductotal)+"\t"
          with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write(out)
          
          found = 0
          #get invioce amount from downloaded files
          with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/DHMO Union.csv") as csvfile:
            medent = csv.reader(csvfile)
            InvoiceType = "DHMO Union"

  #def test_download(medent,deductotal): DHMO Union
            for mrow in medent:
              try:
                invoiceSS = mrow[4]
                if invoiceSS == deductSS:
                  invoicetotal = float(mrow[9])
                  if abs(invoicetotal - deductotal) >= 1:
                    print name + " deduction amount= " + str(deductotal) + " DHMO Union invoice amount= " + str(mrow[9])
                    deductotal = 0
                  found = 1
                  break
              except:
                continue 

            if found == 0:
              with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO 2788.csv") as csvfile:
                medent1 = csv.reader(csvfile)
                InvoiceType = "HMO 2788"

  #def test_download(medent,deductotal): HMO 2788
                for mrow in medent1:
                  try:
                    invoiceSS = mrow[4]
                    if invoiceSS == deductSS:
                      invoicetotal = float(mrow[9])
                      if abs(invoicetotal - deductotal) >= 1:
                        print name + " deduction amount= " + str(deductotal) + " HMO 2788 invoice amount= " + str(mrow[9])
                        deductotal = 0
                      found = 1
                      break
                  except:
                    continue

                if found == 0:
                  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/DHMO.csv") as csvfile:
                      medent2 = csv.reader(csvfile)
                      InvoiceType = "DHMO"

  #def test_download(medent,deductotal):  DHMO
                      for mrow in medent2:
                        try:
                          invoiceSS = mrow[4]
                          if invoiceSS == deductSS:
                            invoicetotal = float(mrow[9])
                            if abs(invoicetotal - deductotal) >= 1:
                              print name + " deduction amount= " + str(deductotal) + " DHMO invoice amount= " + str(mrow[9])
                              deductotal = 0
                            found = 1
                            break
                        except:
                          continue
                      
                      if found == 0:
                        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO 2788 Union.csv") as csvfile:
                          medent3 = csv.reader(csvfile)
                          InvoiceType = "HMO 2788 Union"

  #def test_download(medent,deductotal):  HMO 2788 Union
                          for mrow in medent3:
                            try:
                              invoiceSS = mrow[4]
                              if invoiceSS == deductSS:
                                invoicetotal = float(mrow[9])
                                if abs(invoicetotal - deductotal) >= 1:
                                  print name + " deduction amount= " + str(deductotal) + " HMO 2788 Union invoice amount= " + str(mrow[9])
                                  deductotal = 0
                                found = 1
                                break
                            except:
                              continue

                          if found == 0:                    
                            with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO Union.csv") as csvfile:
                              medent4 = csv.reader(csvfile)
                              InvoiceType = "HMO Union"

  #def test_download(medent,deductotal): HMO Union
                              for mrow in medent4:
                                try:
                                  invoiceSS = mrow[4]
                                  if invoiceSS == deductSS:
                                    invoicetotal = float(mrow[9])
                                    if abs(invoicetotal - deductotal) >= 1:
                                      print name + " deduction amount= " + str(deductotal) + " HMO Union invoice amount= " + str(mrow[9])
                                      deductotal = 0
                                    found = 1
                                    break
                                except:
                                  continue
                        
                              if found == 0:
                                with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO.csv") as csvfile:
                                  medent5 = csv.reader(csvfile)
                                  InvoiceType = "HMO"

  #def test_download(medent,deductotal):  HMO
                                  for mrow in medent5:
                                    try:
                                      invoiceSS = mrow[4]
                                      if invoiceSS == deductSS:
                                        invoicetotal = float(mrow[9])
                                        if abs(invoicetotal - deductotal) >= 1:
                                          print name + " deduction amount= " + str(deductotal) + " HMO invoice amount= " + str(mrow[9])
                                          deductotal = 0
                                        found = 1
                                        break
                                    except:
                                      continue 
          deductotal = 0
          if found == 0:
            print name + " NOT FOUND IN INVOICES."
            InvoiceType = "--"
            invoicetotal = 0
    marker = marker + 1


#BACK
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
      krecon.write("\nNOT FOUND IN DEDUCTIONS")
      SumInvoice = 0
      
#deduction file 0 DHMO UNION
  deductionfile = csv.reader(open(currentfile))
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/DHMO Union.csv") as csvfile:
    invoicefile = csv.reader(csvfile)
    file = "DHMO Union"
    for irow in invoicefile:
      deductionfile = csv.reader(open(currentfile))
      found = 0
      try:
          invoiceSS = irow[4]
      except:
          continue
      for drow in deductionfile:
        deductSS = drow[6]
        if invoiceSS == deductSS:
          found = 1
          break
      if found == 0 and irow[2] != "" and irow[9] != "" and irow[9] != "Total dues":
        print irow[2] + " Not found in deductions " + file + "\t\t" + str(irow[9])
        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write("\n"+str(irow[4])+"\t" + str(irow[2])+"\t\t" +str(irow[9]))
        deductionfile = csv.reader(open(currentfile))
#deduction file 1  HMO 2788
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO 2788.csv") as csvfile:
    deductionfile = csv.reader(open(currentfile))
    invoicefile1 = csv.reader(csvfile)
    file = "HMO 2788"
    for irow in invoicefile1:
      deductionfile = csv.reader(open(currentfile))
      found = 0
      try:
          invoiceSS = irow[4]
      except:
          continue
      for drow in deductionfile:
        deductSS = drow[6]
        if invoiceSS == deductSS:
          found = 1
          break
      if found == 0 and irow[2] != "" and irow[9] != "" and irow[9] != "Total dues":
        print irow[2] + " Not found in deductions " + file + "\t" + str(irow[9])
        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write("\n"+str(irow[4])+"\t" + str(irow[2])+"\t\t" +str(irow[9]))
        deductionfile = csv.reader(open(currentfile))
#deduction file 2 DHMO
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/DHMO.csv") as csvfile:
    deductionfile = csv.reader(open(currentfile))
    invoicefile2 = csv.reader(csvfile)
    file = "DHMO"
    for irow in invoicefile2:
      deductionfile = csv.reader(open(currentfile))
      found = 0
      try:
          invoiceSS = irow[4]
      except:
          continue
      for drow in deductionfile:
        deductSS = drow[6]
        if invoiceSS == deductSS:
          found = 1
          break
      if found == 0 and irow[2] != "" and irow[9] != "" and irow[9] != "Total dues":
        print irow[2] + " Not found in deductions " + file  + "\t" + str(irow[9])
        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write("\n"+str(irow[4])+"\t" + str(irow[2])+"\t\t" +str(irow[9]))
        deductionfile = csv.reader(open(currentfile))
#deduction file 3 HMO 2788 UNION
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO 2788 Union.csv") as csvfile:
    deductionfile = csv.reader(open(currentfile))
    invoicefile3 = csv.reader(csvfile)
    file = "2788"
    for irow in invoicefile3:
      deductionfile = csv.reader(open(currentfile))
      found = 0
      try:
          invoiceSS = irow[4]
      except:
          continue
      for drow in deductionfile:
        deductSS = drow[6]
        if invoiceSS == deductSS:
          found = 1
          break
      if found == 0 and irow[2] != "" and irow[9] != "" and irow[9] != "Total dues":
        print irow[2] + " Not found in deductions " + file + "\t" + str(irow[9])
        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write("\n"+str(irow[4])+"\t" + str(irow[2])+"\t\t" +str(irow[9]))
        deductionfile = csv.reader(open(currentfile))
#deduction file 4  HMO UNION
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO Union.csv") as csvfile:
    deductionfile = csv.reader(open(currentfile))
    invoicefile4 = csv.reader(csvfile)
    file = "HMO Union"
    for irow in invoicefile4:
      deductionfile = csv.reader(open(currentfile))
      found = 0
      try:
          invoiceSS = irow[4]
      except:
          continue
      for drow in deductionfile:
        deductSS = drow[6]
        if invoiceSS == deductSS:
          found = 1
          break
      if found == 0 and irow[2] != "" and irow[9] != "" and irow[9] != "Total dues":
        print irow[2] + " Not found in deductions " + file + "\t" + str(irow[9])
        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write("\n"+str(irow[4])+"\t" + str(irow[2])+"\t\t" +str(irow[9]))
        deductionfile = csv.reader(open(currentfile))
#deduction file 5  HMO
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Downloads/HMO.csv") as csvfile:
    deductionfile = csv.reader(open(currentfile))
    invoicefile5 = csv.reader(csvfile)
    file = "HMO"
    for irow in invoicefile5:
      deductionfile = csv.reader(open(currentfile))  
      found = 0
      try:
          invoiceSS = irow[4]
      except:
          continue
      for drow in deductionfile:
        deductSS = drow[6]
        if invoiceSS == deductSS:
          found = 1
          break
      if found == 0 and irow[2] != "" and irow[9] != "" and irow[9] != "Total dues":
        print irow[2] + " Not found in deductions " + file + "\t" + str(irow[9])
        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write("\n"+str(irow[4])+"\t" + str(irow[2])+"\t\t" +str(irow[9]))
        deductionfile = csv.reader(open(currentfile))
  
  with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
    krecon.write("\n\n" +"Total\t\t"+ str(SumInvoice))      
    
  raw_input("press enter to exit")





test_sums()

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

NE1 = [83.1,86.6,90.3,94.6,96.4,94.6] 
vg1 = [61,69.6,77.9,83.2,88.7,89.2] 
R = [33.4,35,54.4,46.7,42.9,60.3] 
BMF = [59.3,59.3,59.3,59.3,59.3,59.3] 
CR = [0.3,0.4,0.5,0.6,0.7,0.8]
plt.plot(CR,NE1,label="NE") 
plt.plot(CR,vg1,label="VG") 
plt.plot(CR,R,label="Random")
plt.plot(CR,BMF,label="BMF")
plt.xlabel("CR")
plt.ylabel("F1")
plt.xlim([0.3,0.8])

pdf = PdfPages(r"pdf/tuffy_fscore_er.pdf")
plt.savefig(pdf, format='pdf', bbox_inches = 'tight')
plt.show()
pdf.close()
pdf = None


NE1 = [.023,.022,.022,.019,.02,.015] 
vg1 = [.051,.083,0.051,0.047,0.038,0.043] 
R = [0.87,0.75,0.63,0.6,0.81,0.81] 
BMF = [0.07,0.07,0.07,0.07,0.07,0.07] 
CR = [0.3,0.4,0.5,0.6,0.7,0.8]
plt.plot(CR,NE1,label="NE") 
plt.plot(CR,vg1,label="VG") 
plt.plot(CR,R,label="Random")
plt.plot(CR,BMF,label="BMF")
plt.xlabel("CR")
plt.ylabel("KLD")
plt.xlim([0.3,0.8])

pdf = PdfPages(r"pdf/tuffy_KLD_er.pdf")
plt.savefig(pdf, format='pdf', bbox_inches = 'tight')
plt.show()
pdf.close()
pdf = None


NE1 = [] 
vg1 = [] 
R = [] 
BMF = [] 
ifile = open('magician_kld_er.csv','r')

for l in ifile:
	l = l.strip()
	if len(l)  == 0:
		continue
	l = l.split(',')
	NE1.append(float(l[0]))
	vg1.append(float(l[1]))
	R.append(float(l[2]))
	BMF.append(float(l[3]))

plt.plot(CR,NE1,label="NE") 
plt.plot(CR,vg1,label="VG") 
plt.plot(CR,R,label="Random")
plt.plot(CR,BMF,label="BMF")
plt.xlabel("CR")
plt.ylabel("KLD")
plt.xlim([0.3,0.8])

pdf = PdfPages(r"pdf/magician_kld_er.pdf")
plt.savefig(pdf, format='pdf', bbox_inches = 'tight')
plt.show()
pdf.close()
pdf = None
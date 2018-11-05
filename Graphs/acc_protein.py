import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

CR = [0.3,0.4,0.5,0.6,0.7,0.8]
NE1 = [] 
vg1 = [] 
R = [] 
BMF = [] 
ifile = open('tuffy_fscore_protein.csv','r')

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
plt.ylabel("F1")
plt.xlim([0.3,0.8])

pdf = PdfPages(r"pdf/tuffy_fscore_protein.pdf")
plt.savefig(pdf, format='pdf', bbox_inches = 'tight')
plt.show()
pdf.close()
pdf = None




NE1 = [] 
vg1 = [] 
R = [] 
BMF = [] 
ifile = open('tuffy_kld_protein.csv','r')

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

pdf = PdfPages(r"pdf/tuffy_kld_protein.pdf")
plt.savefig(pdf, format='pdf', bbox_inches = 'tight')
plt.show()
pdf.close()
pdf = None


NE1 = [] 
vg1 = [] 
R = [] 
BMF = [] 
ifile = open('magician_kld_protein.csv','r')

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
plt.legend(loc = "upper center", ncol =4)

pdf = PdfPages(r"pdf/magician_kld_protein.pdf")
plt.savefig(pdf, format='pdf', bbox_inches = 'tight')
plt.show()
pdf.close()
pdf = None
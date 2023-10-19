import glob
from string import Template
import os

def readTemp(pathInput):
	with open(pathInput) as file:
		html = file.readlines()
		htmlStr = ''.join(html)

	template = Template(htmlStr)

	return(template)

def makeReport():
	html = ''
	for v in views:
	    # break
	    html = ''
	    mp4s = glob.glob(srcPath + '*{}.mp4'.format(v))
	    mp4s.sort()
	    i = 0
	    I = 1
	    for m in mp4s:
	        if i == 0:
	            html += '<tr>'
	        print(m)
	        html += '''
					<td align="center">
						<video id="vAll" width="400px" height="400px" controls loop>
							<source src="{0}"></source>
							Your browser does not support HTML5 video.
						</video>
					</td>
	                '''.format(m, I)
	        i += 1
	        I += 1
	        if i == 5:
	            html += '</tr>'
	            i = 0
	    reportHtml = reportTemp.substitute(view=v, video=html)
	    with open( savePath + v +'.html', 'w') as file:
	        file.write('%s' % reportHtml)


	html = ''
	for v in views:
	    for s in range(0,8):
	        html = ''
	        mp4s = glob.glob(srcPath + '*{0}_{1}.png'.format(v,s))
	        mp4s.sort()
	        i = 0
	        I = 1
	        for m in mp4s:
	            if i == 0:
	                html += '<tr>'
	            print(m)
	            html += '''
			          <td align="center">
	                    <a href="{0}">
	                    <img style="width: 300px; height: 300px;" alt=""
	                        src="{0}"></td>
	                '''.format(m)
	            i += 1
	            I += 1
	            if i == 5:
	                html += '</tr>'
	                i = 0
	        reportHtml = reportTemp.substitute(view=v, video=html)
	        with open( savePath + v + '_' + str(s) + '.html', 'w') as file:
	            file.write('%s' % reportHtml)


lc = 'fod' # 'fp3'
views = ['top', 'front', 'right', 'btm']
states = range(0,8)
reportTemp = readTemp('template.html')

runSet = [['3_stv0', ['fp3', 'fo5', 'fod']], ['2_stcr', ['fp3', 'fo5', 'fod']]]

srcPath0 = 'U:\\kg01\\src\\cevt_vis\\Rep\\{0}_old\\{1}\\vis\\'
savePath0 = 'U:\\kg01\\src\\cevt_vis\\Rep\\{0}_old\\{1}\\reports\\'

srcPath0 = 'U:\\kg01\\src\\cevt_vis\\Rep\\{0}\\{1}\\vis\\'
savePath0 = 'U:\\kg01\\src\\cevt_vis\\Rep\\{0}\\{1}\\reports\\'
print(runSet)
for s in runSet:
    rls = s[0]
    for lc in s[1]:
        srcPath = srcPath0.format(rls, lc)
        savePath = savePath0.format(rls, lc)
        # print(srcPath0.format(rls, lc))

        if not os.path.isdir(savePath):
            print(savePath0.format(rls, lc))
            os.makedirs(savePath)
        makeReport()
	#break

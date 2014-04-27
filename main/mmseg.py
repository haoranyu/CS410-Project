import re
import os
import sys
class SEG(object):
    def __init__(self):
        _localDir=os.path.dirname(__file__)
        _curpath=os.path.normpath(os.path.join(os.getcwd(),_localDir))
        curpath=_curpath
        self.d = {}
        #self.set([x.rstrip() for x in file(os.path.join(curpath,"geo_dict_main.dic")) ])
        self.set([x.rstrip() for x in file(os.path.join(curpath,"dictionary/main.dic")) ])
        self.specialWords= set([x.rstrip().decode('utf-8') for x in file(os.path.join(curpath,"dictionary/suffix.dic"))])
    def set(self,keywords):
        p = self.d
        q = {}
        k = ''
        for word in keywords:
            word = (chr(11)+word).decode('utf-8')
            if len(word)>5:
                continue
            p = self.d
            ln = len(word)
            for i in xrange(ln-1,-1,-1):
                char = word[i].lower()
                if p=='':
                    q[k] = {}
                    p = q[k]
                if not (char in p):
                    p[char] = ''
                    q = p
                    k = char
                p = p[char]
        pass
    def _binary_seg(self,s):
    	#print "binary "+s
        ln = len(s)
        if ln==1:
            	return s,146
	if ln==2:
		if s[0] in self.specialWords:
			#print "20 "+s
			return [s[1],s[0]],0
		elif s[1] in self.specialWords:
			#print "21 "+s
			return [s[1],s[0]],1
		else:
			return [s[1],s[0]],146
	if ln==4:
		return [s[3],s[1]+s[2],s[0]],146

        R = []
        #for i in xrange(ln,1,-1):
        #    tmp = s[i-2:i]
        #    R.append(tmp) 
	i = 0
	while i < len(s):
		if s[i] in self.specialWords:
			#print "special " + s[i]
			R.append(s[i])
			i+=1
		else:
			R.append(s[i:i+2])
			i+=2
	R.reverse()
	return R,146
    def _pro_unreg(self,piece):
        #print piece
        R = []
        tmp = re.sub(u"。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\?|、|\||“|”|‘|’|；|—|（|）|·|\(|\)|　"," ",piece).split()
        ln1 = len(tmp)
        for i in xrange(len(tmp)-1,-1,-1):
        #for i in xrange(0,len(tmp),1):
		mc = re.split(r"([0-9A-Za-z\-\+#@_\.]+)",tmp[i])
        	for j in xrange(len(mc)-1,-1,-1):
                #for j in xrange(0,len(mc),1):
			r = mc[j]
                	if re.search(r"([0-9A-Za-z\-\+#@_\.]+)",r)!=None:
                		R.append(r)
                	else:
               		 	binary, specialLoc = self._binary_seg(r)
				if len(binary) == 1:
					R.append(binary)
					continue
				if specialLoc == 0:
					if len(R) == 0:
						R.extend(binary)
						continue
					R[-1]+=binary[1]
					#print "sp0R"+R[-1]
					R.append(binary[0])
				elif specialLoc == 1 and j != 0:
					#print "mc"+mc[j-1]
					mc[j-1] = binary[0]+mc[j-1]
					R.append(binary[1])
				else:
					R.extend(binary)
        return R 
    def do_seg(self,text):
        text = text.decode('utf-8','ignore')
        p = self.d
        ln = len(text)
        i = ln 
        j = 0
        z = ln
        q = 0
        recognized = []
        mem = None
        mem2 = None
        while i>j:
            t = text[i-j-1].lower()
            if not (t in p):
                if (mem!=None) or (mem2!=None):
                    if mem!=None:
                        i,j,z = mem
                        mem = None
                    elif mem2!=None:
                        delta = mem2[0]-i
                        if delta>=1:
                            if (delta<5) and (re.search(ur"[\w\u2E80-\u9FFF]",t)!=None):
                                pre = text[i-j]
                                if not (pre in self.specialWords):
                                    i,j,z,q = mem2
                                    del recognized[q:]
                            mem2 = None
                            
                    p = self.d
                    if((i<ln) and (i<z)):
                        unreg_tmp = self._pro_unreg(text[i:z])
                        recognized.extend(unreg_tmp)
                    recognized.append(text[i-j:i])
                    i = i-j
                    z = i
                    j = 0
                    continue
                j = 0
                i -= 1
                p = self.d
                continue
            p = p[t]
            j+=1
            if chr(11) in p:
                if j<=2:
                    mem = i,j,z
                    if (z-i<2) and (text[i-1] in self.specialWords) and ((mem2==None) or ((mem2!=None and mem2[0]-i>1))):
                        mem = None
                        mem2 = i,j,z,len(recognized)
                        p = self.d
                        i -= 1
                        j = 0
                    continue
                p = self.d
                if((i<ln) and (i<z)):
                    unreg_tmp = self._pro_unreg(text[i:z])
                    recognized.extend(unreg_tmp)
                recognized.append(text[i-j:i])
                i = i-j
                z = i
                j = 0
                mem = None
                mem2 = None
        if mem!=None:
            i,j,z = mem
            recognized.extend(self._pro_unreg(text[i:z]))
            recognized.append(text[i-j:i])        
        else:
            recognized.extend(self._pro_unreg(text[i-j:z]))
        return recognized

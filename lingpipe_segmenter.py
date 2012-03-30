#encoding:utf-8
from java.io import FileInputStream
from java.io import ObjectInputStream

import sys

jarfiles = ["/opt/lingpipe-segmenter/lingpipe-4.0.1.jar", "/opt/lingpipe-segmenter/zhToksDemo.jar"]
for jar in jarfiles:
    if jar not in sys.path:
        sys.path.append(jar)
modelfile="/opt/lingpipe-segmenter/mxf_segmenter"
fin = FileInputStream(modelfile);
objin =  ObjectInputStream(fin);
mSpellChecker = objin.readObject()

mSpellChecker.setAllowInsert(True);
mSpellChecker.setAllowMatch(True);
mSpellChecker.setAllowDelete(False);
mSpellChecker.setAllowSubstitute(False);
mSpellChecker.setAllowTranspose(False);

mSpellChecker.setNumConsecutiveInsertionsAllowed(1);

mMaxNBest = 1024;
mSpellChecker.setNBest(mMaxNBest);


# segment a string
#sentence=u"你好世界"
#print mSpellChecker.didYouMean(sentence)

# segment a file

f = open("/home/lxb/corpus/taobao_mobile_utf8.txt")
for line in f:
    line = line.decode("utf-8")
    try:
        print mSpellChecker.didYouMean(line).encode("utf-8")
    except UnicodeEncodeError:
        continue
f.close()

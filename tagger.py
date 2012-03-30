#encoding: utf-8
import sys
segmentjar ="/opt/stanford-postagger/stanford-postagger.jar"
if segmentjar  not in sys.path:
    sys.path.append(segmentjar )
from edu.stanford.nlp.tagger.maxent import MaxentTagger

# note that tagger and segmenter conflict
# they can not be both in the classpath
model = "/home/mxf/stanford-postagger-full-2010-05-19/models/chinese.tagger"
tagger = MaxentTagger(model)
sentence = u"你好 世界"
# tag a sentence
tagger.tagTokenizedString(sentence)

# tag a file
f = open("/home/mxf/test.seg", 'r')
for line in f:
    print tagger.tagTokenizedString(line.decode("utf-8"))

f.close()

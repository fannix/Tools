#encoding:utf-8
"""
Segmenter wrapper for Stanford segmenter
"""
from java.util import Properties
from java.io import File, PrintStream, FileOutputStream
from java.lang import System
import sys

def init_segmenter():
    segmentjar ="/Users/mxf/tools/stanford-chinese-segmenter/seg.jar"
    if segmentjar  not in sys.path:
        sys.path.append(segmentjar )

    from edu.stanford.nlp.ie.crf import CRFClassifier
    props = Properties()
    props.setProperty("sighanCorporaDict", "/Users/mxf/tools/stanford-chinese-segmenter/data/")
    props.setProperty("serDictionary", "/Users/mxf/tools/stanford-chinese-segmenter/data/dict-chris6.ser.gz")
    props.setProperty("inputEncoding", "utf-8")
    props.setProperty("sighanPostProcessing", "true")
    segmenter = CRFClassifier(props)

    #alternatively we could use ctb.gz
    segmenter.loadClassifierNoExceptions("/Users/mxf/tools/stanford-chinese-segmenter/data/pku.gz", props)
    segmenter.flags.setProperties(props)

    return segmenter

def segment_stdin(segmenter):
    """
    segment input string from stdin
    """
    for line in sys.stdin:
        uline = line.decode("utf-8")
        segment_li = segmenter.segmentString(uline)
        print " ".join(segment_li).encode("utf-8")

def segment_file(segmenter, infile, outfile):
    """
    segment the file infile and output to the outfile
    """

    fin = open(infile)
    fout =  open(outfile, 'w')
    for line in fin:
        uline = line.decode("utf-8")
        segment_li = segmenter.segmentString(uline)
        segment_line = " ".join(segment_li).encode("utf-8")
        fout.write(segment_line+"\n")
    fout.close()
    fin.close()


if __name__ == "__main__":
    segmenter = init_segmenter()
    if len(sys.argv) < 2:
        segment_stdin(segmenter)
    else:
        for filename in sys.argv[1:]:
            segment_file(segmenter, filename, filename+".seg")

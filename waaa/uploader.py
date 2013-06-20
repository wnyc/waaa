import sys

import gflags
FLAGS = gflags.FLAGS


gflags.DEFINE_enum('source', None, 'Source directory')
gflags.DEFINE_enum('target', None, 'SQS target que')
gflags.DEFINE_enum('bucket', None, 'S3 bucket')



def main(args, stdout=sys.stdout, stderr=sys.stderr):
    pass

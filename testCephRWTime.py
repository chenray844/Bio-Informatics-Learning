# -*- coding: utf-8 -*-

import unittest
import time
import os
import shutil

class TestCephRWTime(unittest.TestCase):
    def setUp(self):
        self.fileNum = 10
        fdir = 'ceph-data'
        cwd = os.getcwd()
        self.ceph_dir = os.path.join(str(cwd),fdir)
        if not os.access(self.ceph_dir, os.F_OK):
            os.makedirs(self.ceph_dir)

        self.resFname = 'ceph-analysis.dat'

    def tearDown(self):
        start = time.time()
        if os.access(self.ceph_dir, os.F_OK):
            shutil.rmtree(self.ceph_dir)
        end = time.time()

        dt = end - start
        print '\n\n============ Remove Dir =================\n\n'
        print 'spend < %.6f > seconds to remove dir < %s > ' % (dt, self.ceph_dir)

    def test_write(self):
        start = time.time()

        fw = open(self.resFname,'w')
        fw.write('#    Time (s)           Filesize (MB)                 Filename   \n\n')
        sum_t = 0
        max_t = 0
        sum_s = 0
        min_t = 0
        for i in xrange(self.fileNum):
            t1 = time.time()
            fname = 'ceph--%s.dat' % str(i)
            fname = os.path.join(self.ceph_dir, fname)

            with open(str(fname), 'w') as f:
                rnd = 1e5*(i%10.0)
                for n in xrange(int(1e5)+int(rnd)):
                    f.write('%s\n' % n)

            t2 = time.time()
            fsize = os.path.getsize(fname)
            fsize = float(fsize)/1000000.0

            dt = t2 - t1
            if dt > max_t:
                max_t = dt
            if dt < min_t:
                min_t = dt
            sum_t += dt
            sum_s += fsize

            print 'spend < %.6f > seconds in writing file < %s > with file size < %s > MB' % (dt, fname, fsize)
            fw.write('     %.6f         %s             %s \n' % (dt, fsize, fname))


        end = time.time()
        print '\n\n============== Total ===================\n\n'
        print 'spend < %.6f > seconds to write %s files in %s ' % (end-start, self.fileNum, self.ceph_dir)

        fw.write('\n\n'+'='*40+' Total '+'='*40+'\n\n')
        fw.write('#    Spend %.6f seconds to write %s files into %s \n' % (end-start, self.fileNum, self.ceph_dir))
        fw.write('#    Spend %.6f seconds to write %s MB data size in %s dir, And Average Time %.6f spent each file \n' % (sum_t, sum_s, self.ceph_dir, float(sum_t)/float(self.fileNum)))

        fw.close()

if __name__ == '__main__':
    unittest.main()
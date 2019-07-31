import unittest
import os
import filecmp
import numpy as np

dir="data/KondoChain_Stot1_cmp"

def read_out(filename):
    # drop the first two columns
    array = np.loadtxt(filename, dtype='float').astype('float')
    return array

class TestKondoChain_Stot1_cmp(unittest.TestCase):
    def test_KondoChain_Stot1_cmp(self):
        # run
        self.assertIs(0, os.system("../../src/mVMC/vmc.out -s %s/StdFace.def" %dir))        
        # get results
        array_calc = read_out("./output/zqp_opt.dat")[0:2]
        ref_ave = read_out("%s/ref/ref_mean.dat" %dir)[0:2]
        ref_std = read_out("%s/ref/ref_std.dat" %dir)[0:2]
        ref = abs(array_calc - ref_ave)
        testTrue = np.logical_or(abs(3.*ref_std)>ref ,ref<1e-8)
        for _test in testTrue:
            self.assertTrue(_test)
        
if __name__ == '__main__':
    unittest.main()

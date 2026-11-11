import unittest
import numpy as np
from qc_models import state,question,born,joint,qq,update,mixture,classical_order_example,examples

class ModelChecks(unittest.TestCase):
    def test_probability_conservation_and_qq_over_angles(self):
        for s in [0,20,45,90]:
            for a in [0,40,90]:
                for b in [0,50,90]:
                    ab=joint(state(s),question(a),question(b))
                    ba=joint(state(s),question(b),question(a))
                    self.assertAlmostEqual(ab.sum(),1)
                    self.assertTrue((ab>=0).all())
                    self.assertAlmostEqual(qq(ab,ba),0)
    def test_repeated_question_is_consistent(self):
        j=joint(state(37),question(0),question(0))
        self.assertAlmostEqual(j[0,1]+j[1,0],0)
    def test_zero_probability_outcome(self):
        with self.assertRaises(ValueError): update(state(0),question(0)[1])
        np.testing.assert_allclose(joint(state(0),question(0),question(0)),[[1,0],[0,0]],atol=1e-12)
    def test_complex_state(self):
        psi=np.array([1,1j])/np.sqrt(2)
        self.assertAlmostEqual(born(psi,question(0)[0]),.5)
    def test_invalid_inputs(self):
        for P in [np.ones((2,2)),np.array([[1,1],[0,0]])]:
            with self.assertRaises(ValueError): born(state(0),P)
        with self.assertRaises(ValueError): born([2,0],question(0)[0])
        with self.assertRaises(ValueError): qq([[1,1],[0,0]],[[1,0],[0,0]])
        with self.assertRaises(ValueError): mixture(1.1,.7,.3)
    def test_classical_rival_with_zero_qq(self):
        ab,ba=classical_order_example()
        self.assertAlmostEqual(qq(ab,ba),0)
        self.assertAlmostEqual(ab[0,:].sum()-ba[:,0].sum(),-.3)
    def test_bracket_and_direct_comparison(self):
        vals=[mixture(w,.7,.3) for w in np.linspace(0,1,101)]
        self.assertGreaterEqual(min(vals),.3)
        self.assertLessEqual(max(vals),.7)
        e=examples()
        self.assertAlmostEqual(e['direct_rate'],.5+np.sqrt(.21))
        self.assertAlmostEqual(e['assessed_rate'],.5)
        self.assertAlmostEqual(e['geometric_B_first'],.75)
        self.assertAlmostEqual(e['geometric_B_after_A'],.4334888892202555)

if __name__=='__main__': unittest.main()

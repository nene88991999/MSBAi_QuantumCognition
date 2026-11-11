"""Small quantum-probability examples for Modules 1–4.

Adapted from Nathan Yang's quantum cognition manuscript, ch_python_lab.tex.
All numerical examples are imposed models. They are not observations of people.
Angles passed to question() and state() are in degrees.
"""
import numpy as np

def state(angle_degrees):
    """A normalized real two-dimensional state at a stated angle."""
    theta=np.deg2rad(float(angle_degrees))
    if not np.isfinite(theta): raise ValueError('Angle must be finite.')
    return np.array([np.cos(theta),np.sin(theta)])

def _unit(psi):
    psi=np.asarray(psi,dtype=complex)
    if psi.ndim!=1 or not np.all(np.isfinite(psi)):
        raise ValueError('State must be a finite one-dimensional vector.')
    if not np.isclose(np.vdot(psi,psi).real,1,atol=1e-10):
        raise ValueError('State must have squared length one.')
    return psi

def projector(vector):
    """Projector onto a nonzero vector, normalized inside this function."""
    v=np.asarray(vector,dtype=complex)
    if v.ndim!=1 or not np.all(np.isfinite(v)) or np.linalg.norm(v)<1e-12:
        raise ValueError('Supply a finite nonzero vector.')
    v=v/np.linalg.norm(v)
    return np.outer(v,v.conj())

def question(angle_degrees):
    """Return yes and no projectors. Outcome index 0 means yes; 1 means no."""
    yes=projector(state(angle_degrees))
    return yes,np.eye(2)-yes

def born(psi,P):
    """Squared projected length for an orthogonal projector P."""
    psi=_unit(psi);P=np.asarray(P,dtype=complex)
    if P.shape!=(len(psi),len(psi)) or not np.all(np.isfinite(P)):
        raise ValueError('Projector dimensions must match the state.')
    if not np.allclose(P,P.conj().T,atol=1e-10) or not np.allclose(P@P,P,atol=1e-10):
        raise ValueError('P must be an orthogonal projector.')
    projected=P@psi
    return float(np.clip(np.vdot(projected,projected).real,0,1))

def update(psi,P):
    """State conditional on a possible observed outcome.

    A zero-probability outcome has no conditional state. Raise an error rather
    than divide by zero. joint() handles impossible branches without updating.
    """
    p=born(psi,P)
    if p<1e-14: raise ValueError('Cannot condition on a zero-probability outcome.')
    return P@np.asarray(psi,dtype=complex)/np.sqrt(p)

def joint(psi,first,second):
    """Rows are first-question yes/no, columns are second-question yes/no."""
    out=np.zeros((2,2))
    for i,P in enumerate(first):
        p=born(psi,P)
        if p<1e-14: continue
        posterior=update(psi,P)
        for j,Q in enumerate(second): out[i,j]=p*born(posterior,Q)
    if not np.isclose(out.sum(),1): raise ValueError('Questions must partition the state space.')
    return out

def qq(ab,ba):
    """Agreement-share difference. Input tables must each sum to one.

    AB: A rows, B columns. BA: B rows, A columns. Transposing BA to put
    A in rows leaves its diagonal sum unchanged.
    """
    tables=[np.asarray(t,dtype=float) for t in (ab,ba)]
    for t in tables:
        if t.shape!=(2,2) or not np.all(np.isfinite(t)) or (t<0).any() or not np.isclose(t.sum(),1):
            raise ValueError('Use a nonnegative 2 by 2 probability table summing to one.')
    return float(np.trace(tables[0])-np.trace(tables[1]))

def assessed_rate(psi,assessment,action):
    """Marginal yes rate for action after recording the assessment outcome."""
    return float(joint(psi,assessment,action)[:,0].sum())

def mixture(weight,rate_yes,rate_no):
    """Weighted rate under fixed conditional rates; all arguments are probabilities."""
    values=np.asarray([weight,rate_yes,rate_no],dtype=float)
    if not np.isfinite(values).all() or ((values<0)|(values>1)).any():
        raise ValueError('Inputs must lie in [0,1].')
    return float(weight*rate_yes+(1-weight)*rate_no)

def classical_order_example():
    """An explicit classical sequential process with an order effect and q=0.

    A first: P(A=yes)=.4; P(B=yes|A=yes)=.75; P(B=yes|A=no)=1/3.
    B first: P(B=yes)=.5; P(A=yes|B=yes)=.9; P(A=yes|B=no)=.5.
    These are separate context-dependent transition rules, not one unchanged
    joint distribution carried across the two procedures.
    """
    ab=np.array([[.4*.75,.4*.25],[.6/3,.6*2/3]])
    ba=np.array([[.5*.9,.5*.1],[.5*.5,.5*.5]])
    return ab,ba

def examples():
    psi=state(20);A=question(0);B=question(50)
    ab,ba=joint(psi,A,B),joint(psi,B,A)
    classical_ab,classical_ba=classical_order_example()
    coherent=state(45);assessment=question(0)
    action=question(np.rad2deg(np.arccos(np.sqrt(.7))))
    direct=born(coherent,action[0]);assessed=assessed_rate(coherent,assessment,action)
    return {
        'probability_at_37_degrees':born(state(37),question(0)[0]),
        'geometric_B_first':born(psi,B[0]),
        'geometric_B_after_A':float(ab[:,0].sum()),
        'geometric_q':qq(ab,ba),
        'classical_A_first':float(classical_ab[0,:].sum()),
        'classical_A_after_B':float(classical_ba[:,0].sum()),
        'classical_q':qq(classical_ab,classical_ba),
        'direct_rate':direct,'assessed_rate':assessed,
        'direct_minus_assessed':direct-assessed,
        'conditional_rates':[.7,.3],
    }

if __name__=='__main__':
    import json
    print(json.dumps(examples(),indent=2))
    print('These are model illustrations. A matching pattern does not identify a unique mechanism.')

#!/usr/bin/env python3
import math
import random
import sys


question_ = r"""
    A farmer sells his product at a loss of %s\%%. If his S.P. was Rs %s, what was his actual loss? What was his cost price?
"""
answer_ = r"""
    Let the C.P be $x$\\
    We have, S.P. = Rs %s,Loss $= %s\%%$\\
    Loss $= \frac{%s}{100}\times x=\frac{%sx}{%s}$\\
    S.P. = C.P. - Loss\\
    \[%s = x - \frac{%sx}{%s}\]
    \[%s =\frac{%sx}{%s}\]
    \[x =Rs%s\]
    Loss $=%s - %s = Rs %s$\\
"""

Steps = [
  {
    "step": r"""
          $$ \text{ Let the C.P be }  x  $$
          $$ \text { We have, S.P. = Rs } %s,
             \text{ Loss } = %s $$
          """,
    "verifier": "",
    "explain": r""" $$ \text{ Please refer back to  the question. The sales price is
           mentioned as Rs %s and loss percentage as %s percent.  } $$
          """
  },
  {
    "step":  r"""
          $$ \text{ Loss = } \frac{%s}{100}\times
             x=\frac{%sx}{%s} $$
              """,
    "verifier": "",
    "explain": r""" $$ \text {%s percent means } \frac{%s}{100}
             \text{ which becomes } \frac{%s}{%s} \text { after simplification.}  $$
           """
  },
  {
    "step":  r"""
          S.P. = C.P. - Loss
            %s = x - (%sx)/(%s)
            %s = (%sx)/(%s)
              """,
    "verifier": "",
    "explain": r""" Lost is equivalent to difference between Cost price and the Selling Price, 
            i.e. Lost = C.P - S.P 
            => S.P = C.P. - Lost
            here, Cost price (C.P.) = x, Lost Percentage = (%sx)/(%s), Selling Price (S.P.) = %s
    
            => %s = x - (%sx)/(%s)

            On substracting the Lost Percentage from Cost price, we get:
            => %s = (%sx)/(%s)
           """
  },
  {
    "step":  r"""
              => x = (%s)*(%s)/(%s)
              => x = Rs %s
              """,
    "verifier": "",
    "explain": r""" On carrying out the above step, we get the resultant value of x as, 
            x = (%s)*(%s)/(%s)

            Thus the resultant value of the Cost Price (C.P.) is Rs %s.
           """
  },
  {
    "step":  r"""
              => Loss  = (%s) - (%s)
              => Loss = Rs %s
              """,
    "verifier": "",
    "explain": r""" As, the Loss is given by the difference in Cost Price and Selling Price, and we have been given Selling Price, and we successfully   obtained Cost Price in the previous step. 

        Thus, the loss is given by,

        Loss = C.P - S.P
        Loss = (%s) - (%s)
        Loss = (%s)

        Hence, the Loss is Rs %s.

           """
  }]


loss_per = 15
sp = 20000
cp = (sp*100) // (100-loss_per)
h = 5

question = question_ % (loss_per, sp)
answer = answer_ % (sp, loss_per, loss_per, loss_per // h, 100 // h,
                            sp, loss_per // h, 100 // h,
                            sp, 100 // h - loss_per // h, 100 // h, cp,
                            cp, sp, cp - sp)

# add 3 more steps below
step_args = [[sp, loss_per],
             [loss_per, loss_per // h, 100 // h],
             [sp, loss_per // h, 100 // h, sp, 100 // h - loss_per // h, 100 // h],
             [sp, 100 // h, 100 // h - loss_per // h, cp],
             [cp, sp, cp - sp]
             ]

# add 3 more explainer args list below
explainer_args = [[sp, loss_per],
                  [loss_per, loss_per, loss_per // h, 100 // h],
                  [loss_per // h, 100 // h, sp, sp, loss_per // h, 100 // h, sp, 100 // h - loss_per // h, 100 // h],
                  [sp, 100 // h, 100 // h - loss_per // h, cp],
                  [cp, sp, cp - sp, cp - sp]
                  ]

print(question)
print(answer)

i=0
for s in Steps:
  txt = s["step"] % (tuple(step_args[i]))
  print("Step  %s: %s" % (i+1, txt))
  txt = s["explain"] % (tuple(explainer_args[i]))
  print("Explanation of step %s: %s" % (i+1, txt))
  i += 1
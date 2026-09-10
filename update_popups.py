with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

# We need to replace the nested flashcards block with HTML details lists.
# The block currently starts with `card = f"""??? example "Case #{idx+1}: {label}"`
# and ends right before the Eigenvalues.

new_card_str = r'''card = f"""??? example "Case #{idx+1}: {label}"
    <ul style="list-style-type: none; padding-left: 0;">
      <li>
        <details>
          <summary><strong>Ambient Space:</strong> <code>{alg}</code></summary>
          <div style="padding: 5px 10px; margin-top: 5px; background-color: rgba(0,0,0,0.05); border-left: 3px solid #007bff;">
            The ambient flag variety in which the complete intersection is embedded.
          </div>
        </details>
      </li>
      <li>
        <details>
          <summary><strong>Dimension:</strong> {dim}</summary>
          <div style="padding: 5px 10px; margin-top: 5px; background-color: rgba(0,0,0,0.05); border-left: 3px solid #007bff;">
            The complex dimension of the resulting geometric space. Computed by subtracting the rank of the intersecting bundle from the dimension of the ambient space.
          </div>
        </details>
      </li>
      <li>
        <details>
          <summary><strong>Fano Index:</strong> {fano}</summary>
          <div style="padding: 5px 10px; margin-top: 5px; background-color: rgba(0,0,0,0.05); border-left: 3px solid #007bff;">
            The Fano index $I_X$ is the greatest integer dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication.
          </div>
        </details>
      </li>
      <li>
        <details>
          <summary><strong>Basis Rank:</strong> {rank}</summary>
          <div style="padding: 5px 10px; margin-top: 5px; background-color: rgba(0,0,0,0.05); border-left: 3px solid #007bff;">
            The number of dimensions in the projected flag-ambient cohomology ring $H_{{amb}}^*(X)$. This equals the size of the square quantum multiplication matrix.
          </div>
        </details>
      </li>
      <li>
        <details>
          <summary><strong>Eigenvalues:</strong> {", ".join(eigen_strs)}</summary>
          <div style="padding: 5px 10px; margin-top: 5px; background-color: rgba(0,0,0,0.05); border-left: 3px solid #007bff;">
            The eigenvalues of the small quantum multiplication matrix $c_1(TX)\\star$ evaluated at $y=1$, along with their algebraic multiplicities. These values govern the spectrum of the quantum connection.
          </div>
        </details>
      </li>
    </ul>
"""'''

# Regex to find the assignment of `card = f"""??? example ...` up to the end of Eigenvalues block
pattern = r'card = f"""\?\?\? example.*?Eigenvalues:[^\n]*\n"""'

code = re.sub(pattern, new_card_str, code, flags=re.DOTALL)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)

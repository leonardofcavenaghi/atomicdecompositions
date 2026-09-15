from gwflags import FlagVariety
import re
import traceback

specs = {
    # Picard Rank 1
    "1-17": ("A3", [1], []),
    "1-16": ("A4", [1], [[2]]),
    "1-15": ("A4", [2], [[1], [1], [1]]),
    "1-14": ("A5", [1], [[2], [2]]),
    "1-13": ("A4", [1], [[3]]),
    "1-7":  ("A5", [2], [[1], [1], [1], [1], [1]]),
    "1-5":  ("A4", [2], [[1], [1], [2]]),
    "1-4":  ("A6", [1], [[2], [2], [2]]),
    "1-3":  ("A5", [1], [[2], [3]]),
    "1-2":  ("A4", [1], [[4]]),
    "1-6":  ("D5", [5], [[1]] * 7),
    "1-8":  ("C3", [3], [[1]] * 3),
    "1-9":  ("G2", [2], [[1]] * 2),
    # Picard Rank > 1
    "2-24": ("A2xA2", [1, 3], [[1, 2]]),
    # 2-35 is Bl_p(P^3), catalog-only and intentionally omitted.
    "3-27": ("A1xA1xA1", [1, 2, 3], [])
}

results = []
for var_id, (alg, keep, K) in specs.items():
    try:
        X = FlagVariety(alg, keep)
        K_arg = K if len(K) > 0 else None
        fano, betas = X.fano_index_and_betas(K_arg)
        
        # Calculate dimension of complete intersection
        dim_ambient = X.dimension
        bundle_rank = len(K) if K else 0
        dim_ci = dim_ambient - bundle_rank
        
        picard_rank = len(keep)
        
        # Determine expected picard rank from ID (e.g. 1-17 -> 1, 2-24 -> 2)
        expected_pic = int(var_id.split("-")[0])
        
        status = "PASS"
        issues = []
        
        if dim_ci != 3:
            status = "FAIL"
            issues.append(f"Dim={dim_ci} (Expected 3)")
            
        if picard_rank != expected_pic:
            status = "FAIL"
            issues.append(f"Pic={picard_rank} (Expected {expected_pic})")
            
        if fano <= 0:
            status = "FAIL"
            issues.append(f"Not Fano (Index={fano})")
            
        res_str = f"[{status}] {var_id}: alg={alg}, keep={keep}, K={K} -> Dim={dim_ci}, Fano={fano}, Pic={picard_rank}"
        if issues:
            res_str += f" | Issues: {', '.join(issues)}"
            
        print(res_str)
        results.append((var_id, status))
        
    except Exception as e:
        print(f"[ERROR] {var_id}: {str(e)}")
        results.append((var_id, "ERROR"))

failed = [r for r in results if r[1] != "PASS"]
print(f"\nVerification Complete: {len(results)-len(failed)}/{len(results)} Passed.")
if failed:
    print(f"Failed cases: {[r[0] for r in failed]}")

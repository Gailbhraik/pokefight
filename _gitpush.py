import subprocess, os
os.chdir('/home/rakazo/pokemon-battle')
# nettoie les fichiers de travail
for f in ['_new_style.css','_fx3d.js','_patch_fix.py','_patch_design.py','_patch_brace.py','_patch_webgl.py','_check.js']:
    if os.path.exists(f): os.remove(f)
def run(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout[-2000:] if r.stdout else '', r.stderr[-800:] if r.returncode else '')
    return r
run('git','add','-A')
run('git','commit','-m','Refonte design moderne (glassmorphism, typo Outfit) + scene 3D Three.js avec fallback gracieux sans WebGL')
run('git','pull','--rebase','origin','main')
run('git','push','origin','main')
run('git','log','--oneline','-3')

call cd ..
call conda env create -f environment.yml
call conda activate EveryNoise
call ipython kernel install --user --name=EveryNoise
pause
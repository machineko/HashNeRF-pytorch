brew install wget
brew install gmp
brew install qt5
git clone https://github.com/machineko/HashNeRF-pytorch.git
cd HashNeRF-pytorch
pip3 install -r requirements.txt
python3 run_nerf.py --finest_res 512
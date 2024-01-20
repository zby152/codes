clear all
origin_path="Lena.jpg";
test_path='E:\matlab_codes\lab_3\stirmark\Media\Output\Images\Set1\lenna-waved_MEDIAN_3.bmp';
x=2;

wavelet='db6';     %使用的小波函数
N=3;                %小波分解的层数
ratio=0.99;
seed=20;
alpha=0.4;

if(x==1)
    W_SVD_hide(origin_path,wavelet,N,ratio,seed,alpha);
else
    [corr_coef,corr_DCTcoef]=W_SVD_find(origin_path,test_path,wavelet,N,ratio,seed,alpha);
end



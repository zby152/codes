function [corr_coef,corr_DCTcoef]=wavedetectsvd(test,original,seed,level,alpha)
%����˵��:���W-SVDģʽ������ˮӡ�ļ��
%����˵��:
%seed Ϊ���������
%wavelet ʹ�õ�С������
%level ΪС���ֽ�ĳ߶�
%alpha Ϊˮӡǿ��
%ratio Ϊ�㷨��d/n�ı���
%corr_coef,corr_DCTcoef�ֱ�Ϊ��ͬ�����¼��������ֵ

imgorg=imread(original);
imgtest=imread(test);
imgorg=double(imgorg)/255;
imgtest=double(imgtest)/65535;
imgorg=imgorg(:,:,1);
imgtest=imgtest(:,:,1);

%��ȡ����ˮӡ��С����Ƶϵ��
[wmimgrgb,wmimg,wCA,wm2,correlationU,correlationV]=wavemarksvd(original,seed,level,alpha);
%��ȡ����ͼ���С����Ƶϵ��
[C,S]=wavedec2(imgtest,level,'db6');
CA_test=appcoef2(C,S,'db6',level);
%��ȡԭʼͼ���С����Ƶϵ��
[C,S]=wavedec2(imgorg,level,'db6');
CA_ori=appcoef2(C,S,'db6',level);
%��������ˮӡ
realwm=wCA-CA_ori;
testwm=CA_test-CA_ori;
%�������ֵ
corr_coef=trace(realwm'*testwm)/(norm(realwm,'fro')*norm(testwm,'fro'));
%DCTϵ���Ƚ�
DCTrealwm=dct2(wCA-CA_ori);
DCTtestwm=dct2(CA_test-CA_ori);
DCTrealwm=DCTrealwm(1:min(32,max(size(DCTrealwm))),1:min(32,max(size(DCTrealwm))));
DCTtestwm=DCTtestwm(1:min(32,max(size(DCTtestwm))),1:min(32,max(size(DCTtestwm))));
DCTrealwm(1,1)=0;
DCTtestwm(1,1)=0;
corr_DCTcoef=trace(DCTrealwm'*DCTtestwm)/(norm(DCTrealwm,'fro')*norm(DCTtestwm,'fro'));
end

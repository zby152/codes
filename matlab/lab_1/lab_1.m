%实验1.1
result1=3*2;
a=[1,2,3];
% b=[1;2;3];
% result2=a*b;
% 
% %实验1.2
% x=zeros(3,3);
% 
% %实验1.3
% rand('seed',1031);
% result3=rand(5,4);
% result4=randi(4,4,5);
% 
% %实验1.4
% fid=fopen("1.txt","r");
% [msg,msg_len]=fread (fid,4,'uint8');
% 
% %实验1.5
data1=imread("lena_color_512.tif");
% 
% %实验1.6
% imageR=data1(:,:,1);
% 
% %实验1.7
% imageG=data1(:,:,2);
% imageB=data1(:,:,3);
% Mix=cat(3,imageR,imageG,imageB);
% 
% %实验1.8
% %subplot(121),imshow(data1);title('woman'),
% %subplot(122),imshow(data1);title('lena');
% 
% %实验1.9
X=rgb2gray(data1);
% %imshow(X);
% img_b=imbinarize(X);
% %imshow(img_b);
% 
% %实验1.10
% [row,col]=size(data1);
% 
% %实验1.11
% t=0:0.01*pi:2*pi;
% plot(t,sin(t));
% title('0到2∏的正弦曲线','FontSize',16);
% xlabel('t=0到2 ∏');
% ylabel('sin(t)');
% text(pi,sin(pi),'\leftarrow sin(t)=0');
% hold on;
% t=0:0.01*pi:2*pi;
% plot(t,cos(t));
% title('0到2∏的余弦曲线','FontSize',16);
% xlabel('t=0到2 ∏');
% ylabel('cos(t)');
% text(pi,cos(pi),'\leftarrow cos(t)=0');
% hold off

% %实验1.12
% grayImage=rgb2gray(data1);
% dct_image=dct2(grayImage);
% idct_image=idct2(dct_image)/255;
% %imshow(dct_image);
% imshow(idct_image);

%实验1.13
I=im2double(data1);
I=I(:,:,1);
T=dctmtx(8);%生成一个8*8 DCT变换矩阵
B=blkproc(I,[8,8],'P1*x*P2',T,T');
imshow(B);




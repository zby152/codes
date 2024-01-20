% ��������: ����������� W-SVD ģ��������ˮӡ��Ƕ�� 
% �����ʽ����:
%[ watermarkimagergb, watermarkimage, waterCA, watermark, correlationU, correlationV] = wavemarksvd( 'lena.png', 'test.png' , 1983, 'db6' , 2,0.1,0.99) 
% ����˵��:
% input Ϊ����ԭʼͼ�� 
% seed Ϊ��������� 
% wavelet Ϊʹ�õ�С������ 
% level ΪС���ֽ�ĳ߶� 
% alpha Ϊˮӡǿ�� 
% ratio Ϊ�㷨�� d /n �ı��� 
% watermarkimagergb Ϊ����ˮӡ�Ľ��
% watermarkimage Ϊ�����ˮӡ�Ľ�� 
% waterCA Ϊ����ˮӡģ��ĵ�Ƶ�ֽ�ϵ�� 
% watermark2 Ϊ��ˮӡģ��ֱ���ع��õ���ˮӡ��̬, ������ֱ����ʶ, ���������塣 
% correlationU, correlationV Ϊ�滻�����������δ�滻��������������ϵ��
% function watermark = wavemarksvd( input, goal, seed, wavelet, level, alpha, ratio)

input='lena.png';
goal='test.png';
seed=1983;
wavelet='db6';
level=2;
alpha=0.1;
ratio=0.99;






% ��ȡԭʼͼ��
data = imread(input) ;
data = double(data)/255; 
datared = data(:,:,1) ;
% �� R ���ˮӡ 
% ��ԭʼͼ��� R �����С���ֽ��¼ԭʼ��С, �����䲹��������
[C,Sreal] = wavedec2( datared,level,wavelet) ;
[row, list] = size(datared) ;
standard1 = max( row, list) ;
new = zeros( standard1, standard1) ;
if row <= list  
    new( 1:row,:) = datared;
else
    new(:,1:list) = datared;
end 
% ��ʽ��ʼ��ˮӡ 
% С���ֽ�, ��ȡ��Ƶϵ��
[C, S] = wavedec2(new,level,wavelet);
CA = appcoef2(C,S,wavelet,level); 
% �Ե�Ƶϵ�����й�һ������
[M,N] = size( CA) ;
CAmin = min(min( CA) ) ;
CAmax = max(max( CA) ) ;
CA = (1/( CAmax - CAmin) ) * ( CA - CAmin) ;
d = max(size(CA) ) ; 
% �Ե�Ƶ��ϵ����ֵ�ֽ�
[U,sigma,V] =svd(CA); 
% ����������õ�Ҫ�滻��ϵ��������
np = round( d* ratio) ; 
% ���������������������� rand( �� seed�� , seed) ;
rand('seed', seed)
M_V = rand( d, np) - 0.5;
[ Q_V, R_V] = qr( M_V, 0) ;
M_U = rand( d, np) - 0.5;
[ Q_U, R_U] = qr( M_U, 0) ;
% �滻
V2 = V; 
U2 = U; 
V(:, d - np +1: d) = Q_V(:, 1: np) ; 
U(:, d - np +1: d) = Q_U(:, 1: np) ;
sigma_tilda = alpha* flipud(sort( rand( d, 1))) ; 
correlationU = corr2( U, U2) ; 
% �����滻�����ϵ��
correlationV = corr2( V, V2) ; 
% ����ˮӡ 
watermark = U* diag( sigma_tilda, 0) * V ; 
% �ع�����ˮӡ����״, ����ֱ����ʶ, ����������
watermark2 = reshape( watermark,1,S(1,1) * S( 1, 2) ) ;
waterC = C;
waterC( 1, 1: S( 1, 1) * S( 1, 2) ) = watermark2;
watermark2 = waverec2( waterC, S, wavelet) ; 
% ����ϵ������Ƕ��ˮӡ���ͼ��
CA_tilda = CA + watermark;
over1 = find( CA_tilda > 1) ;
below0 = find( CA_tilda < 0) ;
CA_tilda( over1) = 1;
CA_tilda( below0) = 0; 
% ϵ������, ������ϵ���븺������ 
CA_tilda = ( CAmax-CAmin) * CA_tilda +CAmin; 
%ϵ����ԭ����һ����ǰ�ķ�Χ 
% ��¼����ˮӡ�ĵ�Ƶϵ��
waterCA = CA_tilda;
if row <= list  
    waterCA = waterCA(1:Sreal(1,1),:) ;
else
    waterCA = waterCA(:,1:Sreal(1,2) ) ;
end 
% �ع�
CA_tilda = reshape( CA_tilda, 1, S( 1, 1) * S( 1,2) ) ;
C( 1, 1:S( 1, 1) * S( 1, 2) ) = CA_tilda;
watermarkimage = waverec2( C, S, wavelet) ; 
% ��ǰ�油�ϵı�Եȥ��
if row <= list  
    watermarkimage = watermarkimage( 1:row,:) ;
else
    watermarkimage = watermarkimage(:, 1:list) ;
end
watermarkimagergb = data; 
watermarkimagergb(:,:,1) = watermarkimage; 
imwrite( watermarkimagergb, goal,'BitDepth' ,8) ; 
% ͨ��д����������ϵ��
watermarkimagergb2 = imread(goal) ;
figure(1) ; 
subplot( 321) ; imshow( watermark2*255) ; title('ˮӡ��̬ͼ' ) ; 
subplot( 323) ; imshow( data) ; title( ' ԭʼͼ��' ) ; 
subplot( 324) ; imshow( watermarkimagergb2) ; title( 'Ƕ��ˮӡ��� RGB ͼ��' ) ; 
subplot( 325) ; imshow( datared) ; title('R ��ͼ��' ) ;
subplot( 326) ; imshow( watermarkimage) ; title( ' Ƕ��ˮӡ��� R ��ͼ��' ) ; 
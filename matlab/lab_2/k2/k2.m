% k2("scover_LSBR.bmp")
function [ ]=k2(input)
scover=imread(input);

%计算出h数组
h=imhist(scover);

X=zeros(1,127);
sum_X=0;
x_num=0;
for i=1:127
    if(h(2*i-1)+h(2*i)~=0)
        X(i)=((h(2*i-1)-h(2*i))^2)/(2*(h(2*i-1)+h(2*i)));
        x_num=x_num+1;
    end
    sum_X=sum_X+X(i);
end

%sum_X为卡方统计量，x_num为自由度
p=1-chi2cdf(sum_X,x_num);
if(p>0.8)
    disp("图像经过隐写");
else
    disp("图像未经过隐写");
end
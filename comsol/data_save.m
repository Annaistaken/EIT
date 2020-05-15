% refe=[];
% for n = 1:28
%     m = csvread(['D:\\Proj\\EIT\\comsol\\data\\refe',num2str(n),'.csv' ], 8, 1);
%     m = abs(m(1)-m(2));
%     refe = [refe m];
% end
% refe = refe';
% csvwrite('D:\Proj\EIT\EIT-py\data\comsol_refe.csv',refe);

data=[];
for n = 1:28
    m = csvread(['D:\\Proj\\EIT\\comsol\\data\\ru',num2str(n),'.csv' ], 8, 1);
    m = abs(m(1)-m(2));
    data = [data m];
end
data = data';
csvwrite('D:\Proj\EIT\EIT-py\data\comsol_ru.csv',data);

clear all
close all
tabmean
tabls

mediant=meant;
maxt=meant;
mint=meant;

for ni = 2:size(meant,1)
    for ki = 2:size(meant,2)
        mediant(ni,ki)=median(ls(ni,ki,:));
        maxt(ni,ki)=max(ls(ni,ki,:));
        mint(ni,ki)=min(ls(ni,ki,:));
    end
end

hold on
data =meant(2:end,2:end);
%data=mediant(2:end,2:end);
%data =mint(2:end,2:end);
%data =maxt(2:end,2:end);

[k,N]=meshgrid(meant(1,2:end),meant(2:end,1));
surf(k,N,data,'DisplayName','uppmätt värde')

datakol=data(:);%data som kolumnvektor
Nkol=N(:);kkol=k(:);
Nkol(isnan(datakol))=[];
kkol(isnan(datakol))=[];
datakol(isnan(datakol))=[];
A=[Nkol,-((kkol-Nkol/2).^2)./Nkol]\datakol;
a=A(1);b=A(2);
T=N*a-b*((k-N/2).^2)./N;
T=T.*(0*meant(2:end,2:end)+1);
surf(k,N,T,'EdgeColor','r','FaceAlpha',0.7,'DisplayName','uppskattad komplexitet')

T1=N*pi;
surf(k,N,T1,'EdgeColor','g','FaceAlpha',0.5,'DisplayName','\pi*N')
T2=log2(abs(N/2-k)).*N;
surf(k,N,T2,'EdgeColor','b','FaceAlpha',0.5,'DisplayName','log_2(abs(N/2-k))*N')

xlabel('k')
ylabel('N')
zlabel('jämförelser')
legend('show')
view(3)
grid on

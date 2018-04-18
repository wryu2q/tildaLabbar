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
data2 = meant(2:end,2:end)-mediant(2:end,2:end);

[k,N]=meshgrid(meant(1,2:end),meant(2:end,1));
surf(k,N,data,'DisplayName','uppmätt medelvärde')
%surf(k,N,data2,'EdgeColor','r','DisplayName','uppmätt medelvärde-median')

datakol=data(:);%data som kolumnvektor
Nkol=N(:);kkol=k(:);
Nkol(isnan(datakol))=[];
kkol(isnan(datakol))=[];
datakol(isnan(datakol))=[];
A=[Nkol,-((kkol-Nkol/2).^2)./Nkol]\datakol;
a=A(1);b=A(2);
T=N*a-b*((k-N/2).^2)./N ;
T=T.*(0*meant(2:end,2:end)+1);
surf(k,N,T,'EdgeColor','r','FaceAlpha',0.7,'DisplayName',['N*' num2str(a) '-' num2str(b) '*((k-N/2)^2)/N'])

T1=N*pi;
%surf(k,N,T1,'EdgeColor','g','FaceAlpha',0.5,'DisplayName','\pi*N')
T2=log2(abs(N/2-k)).*N;
%surf(k,N,T2,'EdgeColor','b','FaceAlpha',0.5,'DisplayName','log_2(abs(N/2-k))*N')

xlabel('k[Prioritet]')
ylabel('N[Vektorlängd]')
zlabel('Jämförelser')
legend('show')
view(3)
grid on
return
%% 2D plot för fix N
figure(2)
tests=length(ls(1,1,:));
Ni=1;
N=meant(1+Ni,1);
k=meant(1,2:end);
T=meant(1+Ni,2:end);
bar(k,T,1)
xlabel('k [Prioritet]')
xlim([-1,N])
xticks([0 N/4 N/2 3*N/4 N])
xticklabels({'0' ,'N/4' ,'N/2' ,'3*N/4','N'})
ylabel('Medelantal jämförelser [Jämförelser]')
grid on
%ytickformat('%g cmp')
%legend(['T(k,N=' int2str(N) ')'])
return
%% för N=k/konst

figure(3)
hold on
totsteps = length(meant(1,2:end));
for k = meant(1,2:end)
    if k==0
        plotnamn = 'k=0';
    else
        plotnamn = ['k=N*' int2str(k) '/' int2str(totsteps)];
    end
    plot(meant(2:end,1),meant(2:end,k+2),'-','DisplayName', plotnamn )
end
legend('show')
xlabel('N [Vektorlängd]')
ylabel('Medelantal jämförelser [Jämförelser]')
grid on

return

%% fördelning av mätdata
tabls
figure(4)
plot(ls(3,3,:))
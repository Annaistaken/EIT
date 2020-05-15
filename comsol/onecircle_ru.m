function out = model
%
% right_test.m
%
% Model exported on May 14 2020, 17:37 by COMSOL 5.4.0.225.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath('D:\Proj\EIT\comsol');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 2);

model.component('comp1').mesh.create('mesh1');

model.component('comp1').physics.create('ec', 'ConductiveMedia', 'geom1');

model.study.create('std1');
model.study('std1').setGenConv(true);
model.study('std1').create('stat', 'Stationary');
model.study('std1').feature('stat').activate('ec', true);

model.component('comp1').geom('geom1').create('imp1', 'Import');
model.component('comp1').geom('geom1').feature('imp1').set('filename', 'D:\Proj\EIT\comsol\eit8.mphbin');
model.component('comp1').geom('geom1').feature('imp1').importData;
model.component('comp1').geom('geom1').create('c1', 'Circle');
model.component('comp1').geom('geom1').feature('c1').set('type', 'solid');
model.component('comp1').geom('geom1').feature('c1').set('base', 'center');
model.component('comp1').geom('geom1').feature('c1').set('pos', {'0.4' '0.5'});
model.component('comp1').geom('geom1').feature('c1').set('r', '0.2');
model.component('comp1').geom('geom1').run('c1');
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup.create('Enu', 'Young''s modulus and Poisson''s ratio');
model.component('comp1').material('mat1').label('Titanium beta-21S');
model.component('comp1').material('mat1').set('family', 'titanium');
model.component('comp1').material('mat1').propertyGroup('def').label('Basic');
model.component('comp1').material('mat1').propertyGroup('def').set('relpermeability', {'1' '0' '0' '0' '1' '0' '0' '0' '1'});
model.component('comp1').material('mat1').propertyGroup('def').set('electricconductivity', {'7.407e5[S/m]' '0' '0' '0' '7.407e5[S/m]' '0' '0' '0' '7.407e5[S/m]'});
model.component('comp1').material('mat1').propertyGroup('def').set('thermalexpansioncoefficient', {'7.06e-6[1/K]' '0' '0' '0' '7.06e-6[1/K]' '0' '0' '0' '7.06e-6[1/K]'});
model.component('comp1').material('mat1').propertyGroup('def').set('heatcapacity', '710[J/(kg*K)]');
model.component('comp1').material('mat1').propertyGroup('def').set('relpermittivity', {'1' '0' '0' '0' '1' '0' '0' '0' '1'});
model.component('comp1').material('mat1').propertyGroup('def').set('density', '4940[kg/m^3]');
model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', {'7.5[W/(m*K)]' '0' '0' '0' '7.5[W/(m*K)]' '0' '0' '0' '7.5[W/(m*K)]'});
model.component('comp1').material('mat1').propertyGroup('Enu').label('Young''s modulus and Poisson''s ratio');
model.component('comp1').material('mat1').propertyGroup('Enu').set('youngsmodulus', '105e9[Pa]');
model.component('comp1').material('mat1').propertyGroup('Enu').set('poissonsratio', '0.33');
model.component('comp1').material('mat1').set('family', 'titanium');
model.component('comp1').material('mat1').selection.set([1 2 3 4 5 6 7 8]);
model.component('comp1').material.create('mat2', 'Common');
model.component('comp1').material('mat2').selection.set([9]);
model.component('comp1').material('mat2').propertyGroup('def').set('electricconductivity', {'1'});
model.component('comp1').material('mat2').propertyGroup('def').set('relpermittivity', {'1'});
model.component('comp1').material.create('mat3', 'Common');
model.component('comp1').material('mat3').selection.set([10]);
model.component('comp1').material('mat3').propertyGroup('def').set('electricconductivity', {'0.5'});
model.component('comp1').material('mat3').propertyGroup('def').set('relpermittivity', {'1'});

n=0;
num = [13,19,24,18,11,5,1,7];
dot = [21,35,42,34,20,10,3,11];
for i = 1:8 
    for j = i+1:8
        n=n+1;
        %% 设置法向电流密度
        model.component('comp1').physics('ec').create('ncd1', 'NormalCurrentDensity', 1);
        model.component('comp1').physics('ec').feature('ncd1').selection.set(num(i));
        model.component('comp1').physics('ec').feature('ncd1').set('nJ', 1);
        %% 设置接地
        model.component('comp1').physics('ec').create('gnd1', 'Ground', 1);
        model.component('comp1').physics('ec').feature('gnd1').selection.set(num(j));
        %% 求解
        model.sol.create('sol1');
        model.sol('sol1').study('std1');
        
        model.study('std1').feature('stat').set('notlistsolnum', 1);
        model.study('std1').feature('stat').set('notsolnum', '1');
        model.study('std1').feature('stat').set('listsolnum', 1);
        model.study('std1').feature('stat').set('solnum', '1');

        model.sol('sol1').create('st1', 'StudyStep');
        model.sol('sol1').feature('st1').set('study', 'std1');
        model.sol('sol1').feature('st1').set('studystep', 'stat');
        model.sol('sol1').create('v1', 'Variables');
        model.sol('sol1').feature('v1').set('control', 'stat');
        model.sol('sol1').create('s1', 'Stationary');
        model.sol('sol1').feature('s1').create('fc1', 'FullyCoupled');
        model.sol('sol1').feature('s1').feature('fc1').set('linsolver', 'dDef');
        model.sol('sol1').feature('s1').feature.remove('fcDef');
        model.sol('sol1').attach('std1');

        model.result.create('pg1', 'PlotGroup2D');
        model.result('pg1').label([native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'52' 'bf'}), 'unicode') ' (ec)']);
        model.result('pg1').set('frametype', 'spatial');
        model.result('pg1').set('data', 'dset1');
        model.result('pg1').feature.create('surf1', 'Surface');
        model.result('pg1').feature('surf1').set('colortable', 'RainbowLight');
        model.result('pg1').feature('surf1').set('data', 'parent');

        model.sol('sol1').runAll;

        model.result('pg1').run;
        model.result.create('pg2', 'PlotGroup1D');
        model.result('pg2').run;
        %% 导出
        model.result('pg2').create('ptgr1', 'PointGraph');
        model.result('pg2').feature('ptgr1').set('data', 'dset1');
        model.result('pg2').feature('ptgr1').selection.set([dot(i) dot(j)]);
        model.result('pg2').run;
        model.result.export.create('plot1', 'pg2', 'ptgr1', 'Plot');
        model.result.export('plot1').set('filename', [ 'D:\\Proj\\EIT\\comsol\\data\\ru', num2str(n), '.csv' ]);
        model.result.export('plot1').run;
        %% 移除
        model.result.export.remove('plot1');
        model.result('pg2').run;
        model.result('pg2').feature.remove('ptgr1');
        model.result('pg2').run;
        model.result.remove('pg2');

        model.sol.remove('sol1');

        model.component('comp1').physics('ec').feature.remove('gnd1');
        model.component('comp1').physics('ec').feature.remove('ncd1');
    end
end
out = model;

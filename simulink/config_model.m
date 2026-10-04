%% Configuracion del modelo 

g = 9.81; % [m/s^2]

% Masas  =======
m_b = 0.5; % [kg]
m_w = 0.5; % [kg]

% Longitudes 
l_b = 0.2; % [m]
l_w = 0.1; % [m]

% Inercias =====
I_b = 1/12 * m_b * l_b^2; % [kg m^2]
I_w = 1/2 * m_w * l_w^2; % [kg m^2]

M = m_w + 1/2 * m_b; % Masa efectiva potencial 

% Matrices 
I_t = I_b + I_w + l_b^2 * m_b; 

% Valores iniciales 
theta0 = pi/2; 
phi0 = 0; 
dtheta0 = 0;
dphi0 = 0; 

% Viscosidad 




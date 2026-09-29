%[text] # Péndulo invertido Inercial
%[text] ## Coordenadas y Entradas
syms theta phi theta_dot phi_dot tau_w

qs = [theta phi theta_dot phi_dot] %[output:4f766e80]
u = tau_w %[output:2d861601]
%%
%[text] ## Energías
%[text] Cinética
syms I_l I_w m_l m_w l g

T = 1/2 * I_l * theta_dot^2 + I_w * theta_dot * phi_dot + 1/2 * I_w * phi_dot^2 %[output:01ff0eea]
V = 1/2 * m_l * g * l * cos(theta) + 1/2 * m_w * g * l * cos(theta) %[output:89d25710]
%%
%[text] ## Lagrangiano
syms I_l I_w m_l m_w l g

Lan = vpa(T - V) %[output:18b60e5a]
%%
syms t
syms theta(t) phi(t)
syms tau_w(t)
syms theta_ddot phi_ddot

theta_dot = diff(theta,t);
phi_dot   = diff(phi,t);

T = 1/2 * I_l * theta_dot^2 + ...
    I_w * theta_dot * phi_dot + 1/2 * I_w * phi_dot^2;
V = 1/2 * m_l * g * l * cos(theta) + 1/2 * m_w * g * l * cos(theta);

Lan =(T - V);

eulerLagrangeTheta = simplify(diff(diff(Lan, theta_dot), t) - ... %[output:group:275762f1] %[output:06adfeb0]
    diff(Lan, theta)) %[output:group:275762f1] %[output:06adfeb0]

eulerLagrangePhi = simplify(diff(diff(Lan, phi_dot), t) - diff(Lan, phi)) %[output:708d23a6]

M = [I_l I_w; I_w I_w];
q_ddot = [theta_ddot ; phi_ddot];
G = [-1/2 * m_l * g * l * sin(theta) - 1/2 * m_w * g * l * sin(theta); 0];
Torques = [0; tau_w];

EL = M * q_ddot + G == Torques %[output:306fdf64]

[theta_ddot_sol, phi_ddot_sol] = solve(EL,[theta_ddot, phi_ddot]);

theta_ddot_sol = simplify(theta_ddot_sol) %[output:36d11c36]
phi_ddot_sol   = simplify(phi_ddot_sol) %[output:4fb7dca3]

%[appendix]
%---
%[metadata:view]
%   data: {"layout":"inline","rightPanelPercent":49.1}
%---
%[output:4f766e80]
%   data: {"dataType":"symbolic","outputData":{"name":"qs","value":"\\left(\\begin{array}{cccc}\n\\theta  & \\phi  & \\dot{\\theta}  & \\dot{\\phi} \n\\end{array}\\right)"}}
%---
%[output:2d861601]
%   data: {"dataType":"symbolic","outputData":{"name":"u","value":"\\tau_w"}}
%---
%[output:01ff0eea]
%   data: {"dataType":"symbolic","outputData":{"name":"T","value":"\\frac{I_w \\,{\\dot{\\phi} }^2 }{2}+I_w \\,\\dot{\\phi} \\,\\dot{\\theta} +\\frac{I_l \\,{\\dot{\\theta} }^2 }{2}"}}
%---
%[output:89d25710]
%   data: {"dataType":"symbolic","outputData":{"name":"V","value":"\\frac{g\\,l\\,m_l \\,\\cos \\left(\\theta \\right)}{2}+\\frac{g\\,l\\,m_w \\,\\cos \\left(\\theta \\right)}{2}"}}
%---
%[output:18b60e5a]
%   data: {"dataType":"symbolic","outputData":{"name":"Lan","value":"0.5\\,I_w \\,{\\dot{\\phi} }^2 +I_w \\,\\dot{\\phi} \\,\\dot{\\theta} +0.5\\,I_l \\,{\\dot{\\theta} }^2 -0.5\\,g\\,l\\,m_l \\,\\cos \\left(\\theta \\right)-0.5\\,g\\,l\\,m_w \\,\\cos \\left(\\theta \\right)"}}
%---
%[output:06adfeb0]
%   data: {"dataType":"symbolic","outputData":{"name":"eulerLagrangeTheta(t)","value":"I_w \\,\\frac{\\partial^2 }{\\partial t^2 }\\;\\phi \\left(t\\right)+I_l \\,\\frac{\\partial^2 }{\\partial t^2 }\\;\\theta \\left(t\\right)-\\frac{g\\,l\\,m_l \\,\\sin \\left(\\theta \\left(t\\right)\\right)}{2}-\\frac{g\\,l\\,m_w \\,\\sin \\left(\\theta \\left(t\\right)\\right)}{2}"}}
%---
%[output:708d23a6]
%   data: {"dataType":"symbolic","outputData":{"name":"eulerLagrangePhi(t)","value":"I_w \\,{\\left(\\frac{\\partial^2 }{\\partial t^2 }\\;\\phi \\left(t\\right)+\\frac{\\partial^2 }{\\partial t^2 }\\;\\theta \\left(t\\right)\\right)}"}}
%---
%[output:306fdf64]
%   data: {"dataType":"symbolic","outputData":{"name":"EL(t)","value":"\\left(\\begin{array}{c}\nI_w \\,\\ddot{\\phi} +I_l \\,\\ddot{\\theta} -\\frac{g\\,l\\,m_l \\,\\sin \\left(\\theta \\left(t\\right)\\right)}{2}-\\frac{g\\,l\\,m_w \\,\\sin \\left(\\theta \\left(t\\right)\\right)}{2}=0\\\\\nI_w \\,\\ddot{\\phi} +I_w \\,\\ddot{\\theta} =\\tau_w \\left(t\\right)\n\\end{array}\\right)"}}
%---
%[output:36d11c36]
%   data: {"dataType":"symbolic","outputData":{"name":"theta_ddot_sol","value":"\\frac{g\\,l\\,m_l \\,\\sin \\left(\\theta \\left(t\\right)\\right)-2\\,\\tau_w \\left(t\\right)+g\\,l\\,m_w \\,\\sin \\left(\\theta \\left(t\\right)\\right)}{2\\,{\\left(I_l -I_w \\right)}}"}}
%---
%[output:4fb7dca3]
%   data: {"dataType":"symbolic","outputData":{"name":"phi_ddot_sol","value":"-\\frac{I_w \\,g\\,l\\,m_l \\,\\sin \\left(\\theta \\left(t\\right)\\right)-2\\,I_l \\,\\tau_w \\left(t\\right)+I_w \\,g\\,l\\,m_w \\,\\sin \\left(\\theta \\left(t\\right)\\right)}{2\\,I_w \\,{\\left(I_l -I_w \\right)}}"}}
%---

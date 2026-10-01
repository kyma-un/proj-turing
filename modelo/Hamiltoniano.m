%% Langrangiano
syms t
syms theta(t) phi(t)
syms tau_w(t) I_l m_l m_w I_w g L
syms theta_ddot phi_ddot theta_dot phi_dot


dtheta_dot = diff(theta,t);
dphi_dot   = diff(phi,t);

T = 1/2 * I_l * dtheta_dot^2 + ...
    1/2* m_w * (dtheta_dot * L)^2 + 1/2 * I_w * dphi_dot^2;
V = 1/2 * m_l * g * L * cos(theta) + m_w * g * L * cos(theta);

Lan =(T - V);

%% Momentos canónicos
syms p_theta(t) p_phi(t) 

P1 = simplify(diff(Lan, dtheta_dot)) == p_theta
 
P2 = simplify(diff(Lan, dphi_dot)) == p_phi

P1 = subs(P1, diff(theta(t), t), theta_dot )
P2 = subs(P2, diff(phi(t), t), phi_dot)

P1 = solve(P1, theta_dot)
P2 = solve(P2, phi_dot)
%% Hamiltoniano

H = 1/2 * P1 * p_theta + 1/2 * P2 * p_phi + V
H = H - 1/2 * P2 * p_phi

%% Ecuación de Hamilton

d11 = -diff(H, theta) == p_theta
d12 = -diff(H, phi) == p_phi

d21 = -diff(H, p_theta) == theta_dot
d22 = -diff(H, p_phi) == phi_dot
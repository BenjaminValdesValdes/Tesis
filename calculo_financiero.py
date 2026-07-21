# ====================================================================
# EVALUACIÓN ECONÓMICA - RETROFIT TECNOLÓGICO UTEM
# ====================================================================
# Este script modela el Flujo de Caja a 5 años para la implementación 
# de la Capa de Inteligencia (NVIDIA Jetson + Cámara LPR) en el portón.

# 1. Definición de CAPEX (Inversión Inicial)
precio_jetson = 800000        # NVIDIA Jetson Orin Nano 8GB (Valor ref: MCI Electronics)
precio_camara = 738395 * 2    # Cámara IP LPR Dahua ITC413 (x2 Entrada y Salida)
precio_rele = 2300            # Relé Optoacoplado de 1 Canal (Un solo portón bidireccional)
precio_cableado = 23220       # 30m de cable UTP Cat6 100% Cobre para exterior
precio_gabinete = 31500       # Gabinete Metálico Lexo IP65 250x200x150
precio_switch_poe = 55835     # Switch administrable PoE Gigabit (DH-CS4006-4GT-60)
precio_postes = 147084        # 1x Pedestal Metálico CCTV 3m Cónico (Base 250x250)
precio_pvc = 7398             # Tubos Conduit C4 20mm (x4) + Accesorios (Sodimac)
precio_hormigon = 14300       # 5x Sacos de Hormigón Preparado H20 25kg (Topex)
costo_instalacion = 480050    # Mano de obra pura: 2 técnicos x 3 jornadas

capex_total = precio_jetson + precio_camara + precio_rele + precio_cableado + precio_gabinete + precio_switch_poe + precio_postes + precio_pvc + precio_hormigon + costo_instalacion

# 2. Definición de OPEX Anual (Costos Operativos)
costo_electricidad_anual = 33000 # Consumo Jetson+Cámara (Aprox 25W 24/7 a 150 CLP/kWh)
costo_mantencion_anual = 50000   # Limpieza de lentes, revisión de conexiones
opex_total_anual = costo_electricidad_anual + costo_mantencion_anual

# 3. Cálculo de Ahorros (Ingresos del Proyecto)
# Reasignación de conserje: 2 horas/día, 22 días/mes, 12 meses. Valor HH estimado: $3.000
horas_conserje_anual = 2 * 22 * 12
valor_hh_conserje = 3000
ahorro_conserje_anual = horas_conserje_anual * valor_hh_conserje

# 4. Parámetros del Flujo
anos_proyeccion = 5
tasa_descuento = 0.12 # 12% exigido típicamente en proyectos institucionales

# Depreciación lineal a 3 años (solo de los equipos, no de la mano de obra de instalación)
capex_equipos = precio_jetson + precio_camara + precio_rele + precio_cableado + precio_gabinete + precio_switch_poe + precio_postes + precio_pvc
depreciacion_anual = capex_equipos / 3

flujos = [-capex_total] # El Año 0 es la inversión (negativo)

print("==================================================")
print("  EVALUACIÓN ECONÓMICA (PROYECTO RETROFIT UTEM)   ")
print("==================================================")
print(f"CAPEX Total (Inversión): ${capex_total:,.0f} CLP")
print(f"  -> Solo Equipos: ${capex_equipos:,.0f} CLP")
print(f"  -> Instalación: ${costo_instalacion:,.0f} CLP")
print(f"OPEX Anual: ${opex_total_anual:,.0f} CLP")
print(f"Ahorro Anual (Conserje): ${ahorro_conserje_anual:,.0f} CLP")
print(f"Depreciación Anual (Equipos, 3 años): ${depreciacion_anual:,.0f} CLP")
print("--------------------------------------------------")
print("FLUJO DE CAJA A 5 AÑOS:")
print(f"Año 0: ${flujos[0]:,.0f}")

for i in range(1, anos_proyeccion + 1):
    flujo_operativo = ahorro_conserje_anual - opex_total_anual
    flujos.append(flujo_operativo)
    print(f"Año {i}: ${flujo_operativo:,.0f}")

# 5. Cálculo de Indicadores (VAN y TIR) sin usar librerías externas
van = sum(f / (1 + tasa_descuento)**i for i, f in enumerate(flujos))

def calc_tir(flujos, guess=0.1):
    rate = guess
    for _ in range(100):
        npv = sum(f / (1 + rate)**i for i, f in enumerate(flujos))
        derivative = sum(-i * f / (1 + rate)**(i + 1) for i, f in enumerate(flujos))
        if abs(derivative) < 1e-6:
            break
        rate = rate - npv / derivative
    return rate

tir = calc_tir(flujos) * 100

print("--------------------------------------------------")
print(f"VAN (Tasa {tasa_descuento*100}%): ${van:,.0f} CLP")
print(f"TIR: {tir:.2f}%")
print("==================================================")

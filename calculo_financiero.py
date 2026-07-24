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
precio_control = 27800        # Cable de Control Paralelo 2x18 AWG (20m ultra-margen a 1390 c/u)
precio_gabinete = 31500       # Gabinete Metálico Lexo IP65 250x200x150
precio_switch_poe = 55835     # Switch administrable PoE Gigabit (DH-CS4006-4GT-60)
precio_postes = 147084        # 1x Pedestal Metálico CCTV 3m Cónico (Base 250x250)
precio_pvc = 8308             # Tubos Conduit C4 20mm (x5) + Accesorios (Sodimac)
precio_hormigon = 14300       # 5x Sacos de Hormigón Preparado H20 25kg (Topex)
costo_instalacion = 480000    # Mano de obra pura: 2 técnicos x 3 jornadas a 80.000 CLP/día c/u

capex_total = precio_jetson + precio_camara + precio_rele + precio_cableado + precio_control + precio_gabinete + precio_switch_poe + precio_postes + precio_pvc + precio_hormigon + costo_instalacion

# 2. Definición de OPEX Anual (Costos Operativos)
costo_electricidad_anual = 56260 # Consumo Jetson+Cámara
costo_mantencion_anual = 80000   # Limpieza de lentes, revisión de conexiones
opex_total_anual = costo_electricidad_anual + costo_mantencion_anual

# 3. Cálculo de Ahorros (Ingresos del Proyecto)
# Reasignación de conserje: 2 horas/día, 22 días/mes, 12 meses. Valor HH estimado: $3.000
horas_conserje_anual = 2 * 22 * 12
valor_hh_conserje = 4000
ahorro_conserje_anual = horas_conserje_anual * valor_hh_conserje

# 4. Depreciación por Categorías según Normativa SII (Res. Ex. N° 43 / MIDESO)
# - Computación (Jetson, Switch, Relé): 6 años de vida útil normal (SII)
# - Óptica y CCTV (Cámaras LPR Dahua): 7 años de vida útil normal (SII)
# - Infraestructura Pasiva (Pedestal, Gabinete, Cables, PVC, Hormigón): 10 años de vida útil normal (SII)

costo_computacion = precio_jetson + precio_switch_poe + precio_rele        # $858.135 CLP
costo_cctv = precio_camara                                                # $1.476.790 CLP
costo_infraestructura = precio_postes + precio_gabinete + precio_cableado + precio_control + precio_pvc + precio_hormigon # $238.312 CLP

depreciacion_comp_anual = costo_computacion / 6
depreciacion_cctv_anual = costo_cctv / 7
depreciacion_infra_anual = costo_infraestructura / 10

depreciacion_total_anual = depreciacion_comp_anual + depreciacion_cctv_anual + depreciacion_infra_anual

# Valor Libro Remanente (Valor Residual) al Año 5
val_libro_comp_ano5 = costo_computacion - (5 * depreciacion_comp_anual)      # 1 año restante
val_libro_cctv_ano5 = costo_cctv - (5 * depreciacion_cctv_anual)              # 4 años restantes
val_libro_infra_ano5 = costo_infraestructura - (5 * depreciacion_infra_anual) # 5 años restantes

valor_residual_total_ano5 = val_libro_comp_ano5 + val_libro_cctv_ano5 + val_libro_infra_ano5

# 5. Parámetros del Flujo y Proyección
anos_proyeccion = 5
tasa_descuento = 0.055 # 5.5% Tasa Social de Descuento MIDESO (Actualizada en Res. MIDESO 2024)

flujos_operacionales = []
flujos_capitales = [-capex_total]
flujos_netos = [-capex_total]

print("==================================================")
print("  EVALUACIÓN ECONÓMICA OFICIAL (SII / RETROFIT)   ")
print("==================================================")
print(f"CAPEX Total (Inversión Bruta con IVA): ${capex_total:,.0f} CLP")
print(f"  -> Equipos de Cómputo (Vida útil 6 años): ${costo_computacion:,.0f} CLP")
print(f"  -> Óptica y CCTV (Vida útil 7 años): ${costo_cctv:,.0f} CLP")
print(f"  -> Infraestructura Pasiva (Vida útil 10 años): ${costo_infraestructura:,.0f} CLP")
print(f"  -> Mano de Obra Instalación: ${costo_instalacion:,.0f} CLP")
print("--------------------------------------------------")
print(f"OPEX Anual: ${opex_total_anual:,.0f} CLP")
print(f"Ahorro Anual (Conserje): ${ahorro_conserje_anual:,.0f} CLP")
print(f"Depreciación Anual Contable Total: ${depreciacion_total_anual:,.0f} CLP/año")
print(f"Valor Residual Recuperable (Año 5): ${valor_residual_total_ano5:,.0f} CLP")
print("--------------------------------------------------")
print("FLUJO DE CAJA NETO PROYECTADO A 5 AÑOS:")
print(f"Año 0: ${flujos_netos[0]:,.0f}")

for i in range(1, anos_proyeccion + 1):
    f_op = ahorro_conserje_anual - opex_total_anual
    f_cap = valor_residual_total_ano5 if i == anos_proyeccion else 0
    f_neto = f_op + f_cap
    
    flujos_operacionales.append(f_op)
    flujos_capitales.append(f_cap)
    flujos_netos.append(f_neto)
    print(f"Año {i}: ${f_neto:,.0f} (Operacional: ${f_op:,.0f} | Capitales: ${f_cap:,.0f})")

# 6. Cálculo de Indicadores (VAN, TIR y PRC)
van = sum(f / (1 + tasa_descuento)**i for i, f in enumerate(flujos_netos))

def calc_tir(flujos, guess=0.1):
    rate = guess
    for _ in range(100):
        npv = sum(f / (1 + rate)**i for i, f in enumerate(flujos))
        derivative = sum(-i * f / (1 + rate)**(i + 1) for i, f in enumerate(flujos))
        if abs(derivative) < 1e-6:
            break
        rate = rate - npv / derivative
    return rate

tir = calc_tir(flujos_netos) * 100
prc = capex_total / (ahorro_conserje_anual - opex_total_anual)

print("--------------------------------------------------")
print(f"VAN (Tasa {tasa_descuento*100:.1f}% MIDESO): ${van:,.0f} CLP")
print(f"TIR: {tir:.2f}%")
print(f"PRC (Retorno de Inversión): {prc:.2f} años")
print("==================================================")


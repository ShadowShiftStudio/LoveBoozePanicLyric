init python:
    renpy.register_shader("fx.tv_noise_adv", variables="""
        uniform sampler2D tex0;        // базовая картинка
        uniform float u_time;          // время
        uniform vec2  u_model_size;    // размер модели в пикселях
        uniform float u_strength;      // 0..1 — сколько шума поверх
        uniform float u_grain_px;      // размер «гранул» в пикселях (2..8)
        uniform float u_speed;         // скорость анимации
        uniform float u_line_int;      // сила «сканлайнов» (0..1)
        uniform float u_warp;          // горизонтальный дрейф строк (0..0.01)
        uniform float u_color;         // 0..1 — монохром → цветной
        attribute vec2 a_tex_coord;
        varying vec2  v_tex_coord;
    """,
    vertex_300 = "v_tex_coord = a_tex_coord;",
    fragment_functions = """
        float hash12(vec2 p){
            vec3 p3 = fract(vec3(p.xyx) * 0.1031);
            p3 += dot(p3, p3.yzx + 33.33);
            return fract((p3.x + p3.y) * p3.z);
        }
        float vnoise(vec2 p){
            vec2 i = floor(p), f = fract(p);
            vec2 u = f*f*(3.0-2.0*f);
            float a = hash12(i + vec2(0.0,0.0));
            float b = hash12(i + vec2(1.0,0.0));
            float c = hash12(i + vec2(0.0,1.0));
            float d = hash12(i + vec2(1.0,1.0));
            return mix(mix(a,b,u.x), mix(c,d,u.x), u.y);
        }
        float fbm2(vec2 p){
            float n = 0.0;
            n += vnoise(p);
            n += vnoise(p*2.13)*0.5;
            return n / 1.5;
        }
    """,
    fragment_300 = """
        vec2 uv  = v_tex_coord;
        vec2 px  = uv * u_model_size;
        float t  = u_time * u_speed;
        float lineRnd = hash12(vec2(0.0, floor(px.y + t*30.0)));
        float xjitter = (lineRnd - 0.5) * u_warp;
        vec4 base = texture2D(tex0, uv + vec2(xjitter, 0.0));
        vec2 cell = floor(px / u_grain_px);
        float coarse = hash12(cell + floor(t*60.0));
        float fine = fbm2(px*0.75 + vec2(t*55.0, -t*41.0));
        float scan = hash12(vec2(floor(px.y), floor(t*20.0)));
        float spark = step(0.997, hash12(floor(px/8.0) + vec2(floor(t*10.0), 17.0)));
        float mono = 0.58*fine + 0.32*coarse + 0.10*scan;
        mono = mix(mono, 1.0, spark*0.25);
        vec3 colorNoise = vec3(
            mono * (0.85 + 0.15*hash12(px + 31.0 + t*13.0)),
            mono * (0.85 + 0.15*hash12(px + 57.0 - t*19.0)),
            mono * (0.85 + 0.15*hash12(px + 91.0 + t*23.0))
        );
        vec3 noiseRGB = mix(vec3(mono), colorNoise, clamp(u_color, 0.0, 1.0));
        float stripe = 0.66 + 0.34 * sin(px.y*3.14159);
        noiseRGB = mix(noiseRGB, noiseRGB*stripe, u_line_int);
        gl_FragColor = mix(base, vec4(noiseRGB, 1.0), u_strength);
    """)

transform tv_noise(
    strength=0.2,   # сила снега
    grain_px=2.0,   # размер снега
    speed=2.0,      # скорость снега
    line_int=0.5,   # интервал полос искажения  
    warp=0.007,     # сила искажения
    color=0.50      # хз
):
    shader "fx.tv_noise_adv"
    u_strength strength
    u_grain_px grain_px
    u_speed    speed
    u_line_int line_int
    u_warp     warp
    u_color    color

    pause 0.033
    repeat
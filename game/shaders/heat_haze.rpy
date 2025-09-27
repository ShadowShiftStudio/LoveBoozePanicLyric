init python:
    renpy.register_shader("fx.heat_haze_v2", variables="""
        uniform sampler2D tex0;
        uniform float u_time;
        uniform vec2  u_model_size;

        uniform float u_strength;   // 0.0..0.08
        uniform float u_scale;      // 2.0..6.0
        uniform float u_speed;      // 0..1 (нормированная скорость)
        uniform float u_wobble;     // 0..1
        uniform float u_temporal;   // 0..1 — «живость» по времени (доп. турбулентность)
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
        float fbm(vec2 p){
            float n = 0.0;
            n += vnoise(p);
            n += vnoise(p*2.03)*0.5;
            n += vnoise(p*4.07)*0.25;
            return n / 1.75;
        }
    """,
    fragment_300 = """
        vec2 uv = v_tex_coord;

        float speed = clamp(u_speed, 0.0, 1.0);
        float S     = max(u_scale, 0.001);

        float flow = (0.05 + 0.95*speed) * u_time;

        float T = u_temporal; // 0..1
        float t1 = u_time * (0.6 + 1.4*speed);
        float t2 = u_time * (0.8 + 1.8*speed);

        vec2 q  = uv*S + vec2(0.0, flow);

        vec2 w1 = vec2(
            fbm(q*0.5 + vec2(0.0, t1*0.4)),
            fbm(q*0.5 + vec2(0.0, t1*0.7 + 3.14))
        );
        vec2 w2 = vec2(
            fbm(q*0.9 + vec2(0.0, t2*0.5 + 1.57)),
            fbm(q*0.9 + vec2(0.0, t2*0.8 + 4.71))
        );

        float nx = fbm(q + (w1-0.5)*0.35*T + (w2-0.5)*0.20*T) - 0.5;
        float ny = fbm(q*1.13 + (w2-0.5)*0.35*T + (w1-0.5)*0.20*T) - 0.5;

        float wob = 1.0 + 0.15 * u_wobble * sin(u_time*1.2);

        vec2 duv = vec2(nx, ny*1.3) * (u_strength * wob);

        gl_FragColor = texture2D(tex0, uv + duv);
    """)

transform heat_haze(
    strength=0.035,
    scale=3.2,
    speed=0.35,
    wobble=0.6,
    temporal=0.8
):
    shader "fx.heat_haze_v2"
    u_strength strength
    u_scale    scale
    u_speed    speed
    u_wobble   wobble
    u_temporal temporal

    pause 0.016
    repeat


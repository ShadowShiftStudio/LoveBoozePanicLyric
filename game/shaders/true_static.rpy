init python:
    renpy.register_shader("fx.true_static", variables="""
        uniform sampler2D tex0;        // базовая картинка
        uniform float u_time;          // время
        uniform vec2  u_model_size;    // размер в пикселях
        uniform float u_strength;      // 0..1 — доля шума поверх
        uniform float u_fps;           // частота обновления шума (кадров в сек)
        uniform float u_polarity;      // 0=чёрный шум, 0.5=баланс, 1=белый шум
        uniform float u_contrast;      // 0..1 — контраст «зерна»
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
        float contrast01(float x, float k){
            float c = clamp(k, 0.0, 1.0);
            float a = pow(0.5, 1.0 - c);
            return pow(x, a) / ( pow(x, a) + pow(1.0 - x, a) );
        }
        """,
    fragment_300 = """
        vec2 uv = v_tex_coord;
        vec2 px = uv * u_model_size;
        float fps  = max(1.0, u_fps);
        float fid  = floor(u_time * fps);
        float n = hash12( floor(px) + vec2(fid, fid*1.37) );

        n = contrast01(n, clamp(u_contrast, 0.0, 1.0));

        float pol = clamp(u_polarity, 0.0, 1.0);
        float signed = (n - 0.5);                
        float bias   = (pol - 0.5);              
        float v      = clamp(0.5 + signed + bias, 0.0, 1.0);
        vec4 base = texture2D(tex0, uv);
        vec3 noise_rgb = vec3(v);               
        gl_FragColor = mix(base, vec4(noise_rgb, 1.0), clamp(u_strength, 0.0, 1.0));
    """)


transform true_static(
    strength=0.35,    # насколько заметен шум поверх картинки
    fps=45.0,         # как часто «пересдаётся» шум (45 хорошо для «живости»)
    polarity=0.5,     # 0=pepper (чёрный), 0.5=balanced, 1=salt (белый)
    contrast=0.8      # зерно «жёстче» при 0.6..0.9
):
    shader "fx.true_static"
    u_strength strength
    u_fps      fps
    u_polarity polarity
    u_contrast contrast

    # перерисовываемся часто; можно 0.016 для 60 FPS
    pause 0.02
    repeat

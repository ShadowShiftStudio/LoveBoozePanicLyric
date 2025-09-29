init python:
    def decline_surname_male(surname: str, case: str) -> str:
        """
        case: можно передать одно из:
        'именительный','родительный','дательный','винительный','творительный','предложный'
        или сокращения: 'и','р','д','в','т','п'
        или латиницей: 'nom','gen','dat','acc','ins','pre','loc'
        """
        s = (surname or "").strip()
        if not s:
            return s

        # --- утилита: вернуть ту же раскладку букв, что у исходной фамилии
        def recase(src_lower: str, pattern: str) -> str:
            if pattern.isupper():
                return src_lower.upper()
            if pattern[:1].isupper() and pattern[1:].islower():
                return src_lower[:1].upper() + src_lower[1:]
            if pattern.islower():
                return src_lower
            # смешанная раскладка — просто с заглавной первой
            return src_lower[:1].upper() + src_lower[1:]

        # --- нормализация падежа
        c = (case or "").strip().lower()
        cmap = {
            'именительный':'nom','и':'nom','nom':'nom',
            'родительный':'gen','р':'gen','gen':'gen',
            'дательный':'dat','д':'dat','dat':'dat',
            'винительный':'acc','в':'acc','acc':'acc',
            'творительный':'ins','т':'ins','ins':'ins','instrumental':'ins',
            'предложный':'pre','п':'pre','pre':'pre','loc':'pre','locative':'pre'
        }
        key = cmap.get(c)
        if key is None:
            raise ValueError("Неизвестный падеж")
        if key == 'nom':
            return s

        lower = s.lower()
        vowels = 'аеёиоуыэюя'

        # --- чаще всего несклоняемые фамилии
        if lower.endswith(('о','е','ё','и','у','ы','ю','э','ко','их','ых')):
            return recase(lower, s)
        # упрощённо считаем -а/-я иностранными и не склоняем
        if lower.endswith(('а','я')):
            return recase(lower, s)

        # --- прилагательные-типы: -ский/-цкий
        if lower.endswith(('ский','цкий')):
            base = lower[:-4]
            ends = {'gen':'ского','dat':'скому','acc':'ского','ins':'ским','pre':'ском'}
            return recase(base + ends[key], s)

        # --- прилагательные-типы: -ий (мягкий), -ый/-ой (твёрдый)
        if lower.endswith('ий'):
            base = lower[:-2]
            ends = {'gen':'его','dat':'ему','acc':'его','ins':'им','pre':'ем'}
            return recase(base + ends[key], s)
        if lower.endswith(('ый','ой')):
            base = lower[:-2]
            ends = {'gen':'ого','dat':'ому','acc':'ого','ins':'ым','pre':'ом'}
            return recase(base + ends[key], s)

        # --- русские типовые: -ов/-ев/-ёв/-ин/-ын
        if lower.endswith(('ов','ев','ёв','ин','ын')):
            if key in ('gen','acc'):
                form = lower + 'а'
            elif key == 'dat':
                form = lower + 'у'
            elif key == 'ins':
                form = lower + 'ым'
            else:  # pre
                form = lower + 'е'
            return recase(form, s)

        # --- на мягкий знак или -й
        if lower.endswith(('ь','й')):
            stem = lower[:-1]
            ends = {'gen':'я','dat':'ю','acc':'я','ins':'ем','pre':'е'}
            return recase(stem + ends[key], s)

        # --- по умолчанию: на твёрдую согласную
        if lower[-1] not in vowels:
            ends = {'gen':'а','dat':'у','acc':'а','ins':'ом','pre':'е'}
            return recase(lower + ends[key], s)

        # на всякий случай — без изменений
        return recase(lower, s)

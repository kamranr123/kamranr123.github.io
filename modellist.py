# Create the dictionary

Base_config_dictionary = {
  # refer to config.json
  # "CLIP_stop_at_last_layers": 1,
  # "use_scale_latent_for_hires_fix": True,
}

Base_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "ugly, text, logo, monochrome, worst face, (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), horror, geometry, bad_prompt, (bad hands), (missing fingers), multiple limbs, bad anatomy, (interlocked fingers:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), ((2girl)), (deformed fingers:1.2), (long fingers:1.2),(bad-artist-anime), bad-artist, bad hand, extra legs",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 7.0,
}

SD15_model_link = "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/"
SD15_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "sketch, duplicate, ugly, huge eyes, text, logo, monochrome, worst face, (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), horror, geometry, bad_prompt, (bad hands), (missing fingers), multiple limbs, bad anatomy, (interlocked fingers:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), ((2girl)), (deformed fingers:1.2), (long fingers:1.2),(bad-artist-anime), bad-artist, bad hand, extra legs",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

darkSushiMixMix_model_link = "https://huggingface.co/mdl-mirror/dark-sushi-mix/resolve/main/"
darkSushiMixMix_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "sketch, duplicate, ugly, huge eyes, text, logo, monochrome, worst face, (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), horror, geometry, bad_prompt, (bad hands), (missing fingers), multiple limbs, bad anatomy, (interlocked fingers:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), ((2girl)), (deformed fingers:1.2), (long fingers:1.2),(bad-artist-anime), bad-artist, bad hand, extra legs",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

ExpMix_Line_model_link = "https://huggingface.co/mdl-mirror/ExpMix_Line/resolve/main/"
ExpMix_Line_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "sketch, duplicate, ugly, huge eyes, text, logo, monochrome, worst face, (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), horror, geometry, bad_prompt, (bad hands), (missing fingers), multiple limbs, bad anatomy, (interlocked fingers:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), ((2girl)), (deformed fingers:1.2), (long fingers:1.2),(bad-artist-anime), bad-artist, bad hand, extra legs",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

ChameleonAiMix_model_link = "https://huggingface.co/mdl-mirror/chameleon-ai-mix/resolve/main/"
ChameleonAiMix_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "worst quality, low quality:1.4), EasyNegative, bad-artist, bad_prompt_version2",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

majicMIX_realistic_model_link = "https://civitai.com/api/download/models/176425?type=Model&format=SafeTensor&size=pruned&fp=fp16"
majicMIX_realistic_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "easynegative, ng_deepnegative_v1_75t, badhandv4, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), low res, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands)), multiple heads, multiple people",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

#  https://huggingface.co/WarriorMama777/OrangeMixs#aom3
OrangeMixs_model_link = "https://huggingface.co/ckpt/OrangeMixs/resolve/main/"
OrangeMixs_config_dictionary = {
  # refer to config.json
  "CLIP_stop_at_last_layers": 1,
  "use_scale_latent_for_hires_fix": True,
}
OrangeMixs_realistic_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4)",
  "txt2img/Sampling method/value": "DPM++ SDE Karras",
  "txt2img/Sampling steps/value": 24,
  "txt2img/Denoising strength/value": 0.45,
  "txt2img/Upscaler/value": "Latent (nearest-exact)",
}

HenMixReal_model_link = "https://huggingface.co/ckpt/henmixreal/resolve/main/"
HenMixReal_realistic_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "easynegative, ng_deepnegative_v1_75t, badhandv4, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), low res, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands)), multiple heads, multiple people",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

DreamlikePhotoreal_model_link = "https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/"
DreamlikePhotoreal_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "easynegative, ng_deepnegative_v1_75t, badhandv4, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), low res, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands)), multiple heads, multiple people",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

NeverEndingDream2_model_link = "https://huggingface.co/luongphamit/NeverEnding-Dream2/resolve/main/"
NeverEndingDream2_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "easynegative, ng_deepnegative_v1_75t, badhandv4, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), low res, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands)), multiple heads, multiple people",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

F2_model_link = "https://huggingface.co/lilpotat/f2/resolve/main/"
F2_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "easynegative, ng_deepnegative_v1_75t, badhandv4, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), low res, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands)), multiple heads, multiple people",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

PerfectWorld_model_link = "https://huggingface.co/fp16-guy/Perfect_World_v5_fp16_cleaned/resolve/main/"
PerfectWorld_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "easynegative, ng_deepnegative_v1_75t, badhandv4, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), low res, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands)), multiple heads, multiple people",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 10.0,
}

DreamShaper_model_link = "https://huggingface.co/Lykon/DreamShaper/resolve/main/"
DreamShaper_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), (blurry:1.2), (greyscale, monochrome:1.1)",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 8.0,
}

AnyLoRA_model_link = "https://huggingface.co/Lykon/AnyLoRA/resolve/main/"
AnyLoRA_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), (blurry:1.2), (greyscale, monochrome:1.1)",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 8.0,
}

AbsoluteReality_model_link = "https://huggingface.co/Lykon/AbsoluteReality/resolve/main/"
AbsoluteReality_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), (blurry:1.2), BadDream, (UnrealisticDream:1.2)",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 8.0,
}

MeinaHentai_model_link = "https://huggingface.co/Meina/MeinaHentai/resolve/main/"
MeinaHentai_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, zombie, extra limbs, ",
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8.0,
}

MeinaHentai_model_link = "https://huggingface.co/Meina/MeinaHentai/resolve/main/"
MeinaHentai_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, zombie, extra limbs, ",
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8.0,
}

KenCanMix_model_link = "https://huggingface.co/digiplay/kencanmix_v2.0beta/resolve/main/"
KenCanMix_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, zombie, extra limbs, ",
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8.0,
}

HenmixArt_model_link = "https://huggingface.co/digiplay/HenmixArt_v1/resolve/main/"
HenmixArt_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, zombie, extra limbs, ",
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8.0,
}

Reliberate_model_link = "https://huggingface.co/XpucT/Reliberate/resolve/main/"
Reliberate_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, zombie, extra limbs, ",
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8.0,
}

Deliberate_model_link = "https://huggingface.co/XpucT/Deliberate/resolve/main/"
Deliberate_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, zombie, extra limbs, ",
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8.0,
}

Henmix_Real_model_link = "https://huggingface.co/philz1337/henmixreal/resolve/main/"
Henmix_Real_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, extra limbs, Drawings, abstract art, cartoons, surrealist painting, conceptual drawing, graphics, (low resolution:1.4), (blurry:1.3), (strabismus:1.1), (thick thighs:1.2), collage, (makeup:0.8), nsfw, bad proportions, earings, floral print, loli, big eyes, (watermark:1.2), letter, (abs:1.2),",
  "txt2img/Sampling method/value": "DPM++ SDE Karras",
  "txt2img/CFG Scale/value": 8,
}

RunFX_model_link = "https://huggingface.co/digiplay/RunDiffusionFXPhotorealistic_v1/resolve/main/"
RunFX_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(worst quality, low quality:1.4), monochrome, extra limbs,",
  "txt2img/Sampling method/value": "DPM++ SDE Karras",
  "txt2img/CFG Scale/value": 5,
}

Paragon_model_link = "https://huggingface.co/SG161222/Paragon_V1.0/resolve/main/"
Paragon_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "earings, (deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, mutated hands and fingers:1.4), (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, disconnected limbs, mutation, mutated, ugly, disgusting, amputation, easynegative, bad-hands-5",
  "txt2img/Sampling method/value": "DPM++ SDE Karras",
  "txt2img/CFG Scale/value": 7,
}

Photon_model_link = "https://huggingface.co/digiplay/Photon_v1/resolve/main/"
Photon_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "cartoon, painting, illustration, (worst quality, low quality, normal quality:2)",
  "txt2img/Sampling method/value": "DPM++ 2M Karras",
  "txt2img/CFG Scale/value": 6,
}

RealisticVision_model_link = "https://huggingface.co/SG161222/Realistic_Vision_V5.0_noVAE/resolve/main/"
RealisticVision_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck",
  "txt2img/Sampling method/value": "DPM++ SDE Karras",
  "txt2img/CFG Scale/value": 6,
}

SDXL_model_link = "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/"
SDXL_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": '(worst quality, low quality:1.4), monochrome, extra limbs,',
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8,
}

SDXL_Refiner_model_link = "https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/"
SDXL_Refiner_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": '(worst quality, low quality:1.4), monochrome, extra limbs,',
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 8,
}

SDVN6_RealXL_model_link = "https://civitai.com/api/download/models/134461"
SDVN6_RealXL_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": '(worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), tooth, open mouth,',
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 6,
}

DynaVisionXL_model_link = "https://civitai.com/api/download/models/136761"
DynaVisionXL_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": '(worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), tooth, open mouth,',
  "txt2img/Sampling method/value": "Euler a",
  "txt2img/CFG Scale/value": 6,
}

RealCartoonRealistic_model_link = "https://civitai.com/api/download/models/132902"
RealCartoonRealistic_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Negative prompt/value": '(worst quality, low quality, illustration, painting, sketch)',
  "txt2img/Sampling method/value": "DPM++ SDE Karras",
  "txt2img/CFG Scale/value": 6,
}

CounterfeitXL_model_link = "https://civitai.com/api/download/models/146761"
CounterfeitXL_ui_config_dictionary = {
  # refer to ui-config.json
  "txt2img/Sampling method/value": "DPM++ SDE Karras",
  "txt2img/CFG Scale/value": 6,
}

ZavyChromaXL_model_link = "https://civitai.com/api/download/models/149243"
DreamShaperXL10_model_link = "https://civitai.com/api/download/models/149243"
_3DAnimationDiffusion_model_link = "https://civitai.com/api/download/models/128046"
FaeTastic_model_link = "https://civitai.com/api/download/models/105796?type=Model&format=SafeTensor&size=full&fp=fp16"
naturalsin_model_link = 'https://civitai.com/api/download/models/160989'

available_model_dict = {
    'Stable Diffusion v1.5': ['1.5', SD15_ui_config_dictionary, Base_config_dictionary, SD15_model_link, 'v1-5-pruned.safetensors', 'v1-5-pruned-emaonly.safetensors'],
    'Dark Sushi Mix': ['1.5', darkSushiMixMix_ui_config_dictionary, Base_config_dictionary, darkSushiMixMix_model_link, 'darkSushiMixMix_brighterPruned.safetensors', 'darkSushiMixMix_darkerPruned.safetensors'],
    'ExpMix Line': ['1.5', ExpMix_Line_ui_config_dictionary, Base_config_dictionary, ExpMix_Line_model_link, 'expmixLine_v20.safetensors'],
    'ChameleonAiMix': ['1.5', ChameleonAiMix_ui_config_dictionary, Base_config_dictionary, ChameleonAiMix_model_link, 'chameleonaiMix_v10.safetensors'],
    'majicMIX realistic': ['1.5', majicMIX_realistic_ui_config_dictionary, Base_config_dictionary, majicMIX_realistic_model_link, 'majicmixRealistic_v7.safetensors' ],
    'OrangeMixs': ['1.5', OrangeMixs_realistic_ui_config_dictionary, OrangeMixs_config_dictionary, OrangeMixs_model_link, 'AOM3.safetensors','AOM3A1.safetensors', 'AOM3A2.safetensors', 'AOM3A3.safetensors' ],
    'HenMixReal': ['1.5', HenMixReal_realistic_ui_config_dictionary, Base_config_dictionary, HenMixReal_model_link, 'henmixReal_v40.safetensors' ],
    'DreamlikePhotoreal': ['1.5', DreamlikePhotoreal_ui_config_dictionary, Base_config_dictionary, DreamlikePhotoreal_model_link, 'dreamlike-photoreal-2.0.safetensors' ],
    'NeverEndingDream2': ['1.5', NeverEndingDream2_ui_config_dictionary, Base_config_dictionary, NeverEndingDream2_model_link, 'NeverEndingDream_fp16.safetensors', 'NeverEndingDream_ft_mse-inpainting.inpainting.safetensors' ],
    'F2': ['1.5', F2_ui_config_dictionary, Base_config_dictionary, F2_model_link, 'f2.ckpt' ],
    'PerfectWorldV4B': ['1.5', PerfectWorld_ui_config_dictionary, Base_config_dictionary, PerfectWorld_model_link, 'perfectWorld_v5Baked_fp16.safetensors' ],
    'DreamShaper': ['1.5', DreamShaper_ui_config_dictionary, Base_config_dictionary, DreamShaper_model_link, 'DreamShaper_8_INPAINTING.inpainting.safetensors', 'DreamShaper_8_pruned.safetensors' ],
    'AnyLoRA': ['1.5', AnyLoRA_ui_config_dictionary, Base_config_dictionary, AnyLoRA_model_link, 'AAM_Anylora_AnimeMix.safetensors', 'AnyLoRA_noVae_fp16-pruned.ckpt' ],
    'AbsoluteReality': ['1.5', AbsoluteReality_ui_config_dictionary, Base_config_dictionary, AbsoluteReality_model_link, 'AbsoluteReality_1.8.1_pruned.safetensors' ],
    'MeinaHentai': ['1.5', MeinaHentai_ui_config_dictionary, Base_config_dictionary, MeinaHentai_model_link, 'meinaHentai V3 - baked VAE.safetensors' ],
    'KenCanMix': ['1.5', KenCanMix_ui_config_dictionary, Base_config_dictionary, KenCanMix_model_link, 'kencanmix_v20Beta.safetensors' ],
    'HenmixArt': ['1.5', HenmixArt_ui_config_dictionary, Base_config_dictionary, HenmixArt_model_link, 'henmixArt_v10.safetensors' ],
    'Reliberate': ['1.5', Reliberate_ui_config_dictionary, Base_config_dictionary, Reliberate_model_link, 'Reliberate.safetensors', 'Reliberate-inpainting.safetensors' ],
    'Deliberate': ['1.5', Deliberate_ui_config_dictionary, Base_config_dictionary, Deliberate_model_link, 'deliberate_v2.ckpt' ],
    'HenmixReal': ['1.5', Henmix_Real_ui_config_dictionary, Base_config_dictionary, Henmix_Real_model_link, 'henmixReal_v40.safetensors' ],
    'RunDiffusionFXPhotorealistic': ['1.5', RunFX_ui_config_dictionary, Base_config_dictionary, RunFX_model_link, 'rundiffusionFX_v10.safetensors' ],
    'Paragon-V1.0': ['1.5', Paragon_ui_config_dictionary, Base_config_dictionary, Paragon_model_link, 'Paragon_1.0_Beta.safetensors', 'Paragon_1.0_Beta-inpainting.safetensors' ],
    'Photon': ['1.5', Photon_ui_config_dictionary, Base_config_dictionary, Photon_model_link, 'photon_v1.safetensors' ],
    'RealisticVision': ['1.5', RealisticVision_ui_config_dictionary, Base_config_dictionary, RealisticVision_model_link, 'Realistic_Vision_V5.0.safetensors', 'Realistic_Vision_V5.0-inpainting.safetensors' ],
    'SDXL-V1.0 Base': ['xl', SDXL_ui_config_dictionary, Base_config_dictionary, SDXL_model_link, 'sd_xl_base_1.0.safetensors', 'sd_xl_base_1.0_0.9vae.safetensors' ],
    'SDXL-V1.0 Refiner': ['xl', SDXL_Refiner_ui_config_dictionary, Base_config_dictionary, SDXL_Refiner_model_link, 'sd_xl_refiner_1.0_0.9vae.safetensors', 'sd_xl_base_1.0_0.9vae.safetensors' ],
    'SDVN6-RealXL': ['xl', SDVN6_RealXL_ui_config_dictionary, Base_config_dictionary, SDVN6_RealXL_model_link, 'sdvn6Realxl_detailface.safetensors' ],
    'DynaVisionXL': ['xl', DynaVisionXL_ui_config_dictionary, Base_config_dictionary, DynaVisionXL_model_link, 'DynaVisionXL.safetensors' ],
    'RealCartoon-Realistic': ['1.5', RealCartoonRealistic_ui_config_dictionary, Base_config_dictionary, RealCartoonRealistic_model_link, 'RealCartoon-Realistic.safetensors' ],
    'CounterfeitXL-anime': ['xl', CounterfeitXL_ui_config_dictionary, Base_config_dictionary, CounterfeitXL_model_link, 'CounterfeitXL-anime.safetensors' ],
    'ZavyChromaXL': ['xl', Base_ui_config_dictionary, Base_config_dictionary, ZavyChromaXL_model_link, 'ZavyChromaXL_1.0.safetensors' ],
    'DreamShaperXL1.0': ['xl', Base_ui_config_dictionary, Base_config_dictionary, DreamShaperXL10_model_link, 'DreamShaperXL1.0.safetensors' ],
    '3DAnimationDiffusion': ['1.5', Base_ui_config_dictionary, Base_config_dictionary, _3DAnimationDiffusion_model_link, '3DAnimationDiffusionV1.safetensors' ],
    'FaeTastic': ['1.5', Base_ui_config_dictionary, Base_config_dictionary, FaeTastic_model_link, 'FaeTasticV2.safetensors' ],
    'naturalsin': ['1.5', Base_ui_config_dictionary, Base_config_dictionary, naturalsin_model_link, 'naturalsin.safetensors' ],

}

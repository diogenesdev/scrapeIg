from instascrape import *
import os
import glob
import os.path
import zipfile
from flask import send_file
# import wget


# def search_hashtag(tag_name):
#     s_hashtag = Hashtag('https://www.instagram.com/explore/tags/' + tag_name)
#     s_hashtag.scrape()

#     recents = s_hashtag.get_recent_posts()    #os últimos 61 posts com a hashtag
#     s_hashtag_photos = [post for post in recents if not post.is_video]

#     #download images
#     counter = 0
#     nome_pasta_hashtag = "images_hashtags"
#     path = os.getcwd()
#     path = os.path.join(path, nome_pasta_hashtag)

#     if not os.path.exists(path):
#         os.makedirs(path)

#     for post in s_hashtag_photos:
#         fname = "image_"+tag_name+"_"+ str(counter)
#         save_as = os.path.join(path, f"{fname}.png")
#         post.download(save_as)

#         # fname = "image_"+tag_name+"_"+ str(counter)
#         # post.download(f"{fname}.png")
#         counter +=1
#     input("Busca concluída! As imagens estão salvas em "+ path.upper() +". Pressione ENTER para sair...")
#     return s_hashtag_photos

# def search_profile(username):
# if (username == ""):
#     mensagem = "Nada encontrado"
#     return mensagem
# else:
#     # # INÍCIO tratamento para muultiplas requisições e bloqueio do IG
#     # SESSIONID = '2362081507%3AGjqlyUlDlh9QS1%3A15'
#     # headers = {
#     #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/79.0.309.43",
#     #     "cookie": f'sessionid={SESSIONID};'
#     # }

#     # req = requests.get('https://www.instagram.com/'+username, headers=headers)

#     # profile = Profile(req.text)
#     # FIM DO TRATAMENTO
# def search_profile(username):
#     profile = Profile('https://www.instagram.com/'+username)
#     profile.scrape()
#     recents = profile.get_recent_posts()
#     profile_photos = [post for post in recents if not post.is_video]

#     # download images
#     counter = 0
#     nome_pasta_profile = "images_profile"
#     path = os.getcwd()
#     path = os.path.join(path, nome_pasta_profile)

#     # verify if exists 'directory'
#     if not os.path.exists(path):
#         os.makedirs(path)
#     else:
#         filelist = glob.glob(os.path.join(nome_pasta_profile, "*.png"))
#         for f in filelist:
#             os.remove(f)

#     for post in profile_photos:
#         fname = "image_"+username+"_" + str(counter)
#         save_as = os.path.join(path, f"{fname}.png")
#         post.download(save_as)

#         counter += 1
#     # input("Busca concluída! As imagens estão salvas em "+ path.upper() + ". Pressione ENTER para sair...")
#     arquivo_zip = zip_files(nome_pasta_profile)  # zipando arquivos
#     return arquivo_zip
#     # return profile_photos

def search_profile(username):
    profile = Profile('https://www.instagram.com/'+username)
    profile.scrape()
    recents = profile.get_recent_posts()
    profile_photos = [post for post in recents if not post.is_video]

    # download images
    counter = 0
    nome_pasta_profile = "images_profile"
    path = os.getcwd()
    path = os.path.join(path, nome_pasta_profile)

    # verify if exists 'directory'
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        filelist = glob.glob(os.path.join(nome_pasta_profile, "*.png"))
        for f in filelist:
            os.remove(f)

    for post in profile_photos:
        fname = "image_"+username+"_" + str(counter)
        save_as = os.path.join(path, f"{fname}.png")
        post.download(save_as)

        counter += 1

# def zipando_arquivos(nome_pasta_profile):
#      # zipando arquivos
#     zipfolder = zipfile.ZipFile(nome_pasta_profile+'.zip','w', compression = zipfile.ZIP_STORED)

#     # zip all the files which are inside in the folder
#     for root,dirs, files in os.walk(nome_pasta_profile+'/'):
#         for file in files:
#             zipfolder.write(nome_pasta_profile+'/'+file)
#     zipfolder.close()

#     return send_file(nome_pasta_profile+'.zip',
#             mimetype = 'zip',
#             attachment_filename= nome_pasta_profile+'.zip',
#             as_attachment = True)


#    # create a ZipFile object
#     zip_folder = 'imagens.zip'
#     with ZipFile(zip_folder, 'w') as zipObj:
#         # Iterate over all the files in directory
#         for folder_name, subfolders, file_names in os.walk(dir_name):
#             for file_name in file_names:
#                 # create complete file_path of file in directory
#                 file_path = os.path.join(folder_name, file_name)
#                 # Add file to zip
#                 zipObj.write(file_path)
#         zipObj.close()
#         return send_file(zip_folder, mimetype = 'zip', attachment_filename=zip_folder, as_attachment = True)


#   Na V1.1 haverá a verificação se por nome ou hashtag

# def verify_search_type(opcao):
#     not_found_msg = "Tipo de busca inválido"
#     if(opcao == "perfil"):
#         return search_profile(opcao)
#     elif(opcao == "hashtag"):
#         return search_hashtag(opcao)
#     else:
#         return not_found_msg
